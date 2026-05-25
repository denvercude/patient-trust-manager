"""
Checklist page.

Displays the default home view for the daily workflow checklist.
"""

import customtkinter as ctk


CHECKLIST_SECTIONS = (
    (
        "Opening setup",
        (
            "Grab safe key",
            "Collect deposit envelopes",
            "Collect petty cash quarters sheet",
            "Collect ins and outs sheet",
        ),
    ),
    (
        "Store closing review",
        (
            "Review previous evening closing packet",
            "Verify store books match ComCash totals",
            "Count cash drawer",
            "Count cigarettes",
            "File completed store closing paperwork",
        ),
    ),
    (
        "Patient status updates",
        (
            "Process admissions from ins and outs",
            "Process discharges from ins and outs",
            "Update patient phases as needed",
        ),
    ),
    (
        "Deposit preparation",
        (
            "Generate daily deposit sheet",
            "Review deposit sheet for accuracy",
            "Add store balance deposits as needed",
        ),
    ),
    (
        "Store list preparation",
        (
            "Generate daily store list",
            "Update spent at store amounts from store books",
            "Update quarters amounts from petty cash sheet",
            "Apply deposit amounts to patient store balances",
            "Check weekly $100 allowance cap",
            "Run Thursday replenishment if applicable",
            "Review left list and final store list totals",
        ),
    ),
    (
        "Withdrawal preparation",
        (
            "Generate withdrawal sheet from store list",
            "Add manual discharge or special-case withdrawals",
            "Review withdrawal sheet totals",
        ),
    ),
    (
        "Database posting",
        (
            "Copy deposit values to automated deposits sheet",
            "Copy withdrawal values to automated withdrawals sheet",
            "Run add deposits script",
            "Run add withdrawals script",
            "Review script output for errors or duplicates",
        ),
    ),
    (
        "Reconciliation",
        (
            "Open Client Trust Balance sheet",
            "Verify deposits and withdrawals were applied correctly",
            "Check for negative balances",
            "Confirm final trust total balances",
        ),
    ),
    (
        "Final delivery",
        (
            "Print updated store list",
            "Send store list to campus store",
            "File completed paperwork",
        ),
    ),
)


class ChecklistPage(ctk.CTkScrollableFrame):
    """
    Main dashboard page for the daily workflow checklist.
    """

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color="#1a1d24",
        )

        ctk.CTkLabel(
            self,
            text="DAILY CHECKLIST",
        ).pack(padx=25, anchor="w")

        self.sections_container = ctk.CTkFrame(
            self,
            fg_color="transparent",
        )

        self.sections_container.pack(
            fill="both",
            expand=True,
            padx=25,
            pady=(0, 15),
        )

        self._section_frames = []
        self._checkboxes = []
        self._last_layout_width = 0

        self.sections_container.bind(
            "<Configure>",
            self._on_container_resize,
        )

        for section_title, section_items in CHECKLIST_SECTIONS:
            self._add_section(section_title, section_items)

        self._layout_sections()

    def _add_section(self, title, items):
        section_frame = ctk.CTkFrame(
            self.sections_container,
            fg_color="transparent",
        )

        ctk.CTkLabel(
            section_frame,
            text=title,
        ).pack(pady=10, anchor="w")

        for item_label in items:
            check_box = ctk.CTkCheckBox(
                section_frame,
                text=item_label,
            )

            check_box.pack(
                anchor="w",
                fill="x",
                pady=4,
            )

            self._checkboxes.append(check_box)

        self._section_frames.append(section_frame)

    def _layout_sections(self):
        width = self.sections_container.winfo_width()

        if width < 2:
            return

        for frame in self._section_frames:
            frame.grid_forget()

        min_column_width = 430
        cols = min(3, max(1, width // min_column_width))

        for c in range(4):
            self.sections_container.grid_columnconfigure(
                c,
                weight=0,
                uniform="",
            )

        for c in range(cols):
            self.sections_container.grid_columnconfigure(
                c,
                weight=1,
                uniform="checklist",
            )

        for i, frame in enumerate(self._section_frames):
            row = i // cols
            col = i % cols

            frame.grid(
                row=row,
                column=col,
                sticky="nsew",
                padx=8,
                pady=8,
            )

        wrap = max(180, (width // cols) - 80)

        for checkbox in self._checkboxes:
            checkbox.configure(wraplength=wrap)

    def _on_container_resize(self, event):
        if event.width == self._last_layout_width:
            return

        self._last_layout_width = event.width
        self._layout_sections()