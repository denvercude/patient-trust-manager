"""
Checklist page.
Displays the default home view for the daily workflow checklist.
"""

import customtkinter as ctk

from app.gui.theme import (
    COLOR_BG_MAIN,
    CARD_BG,
    CARD_BORDER,
    TEXT_PRIMARY,
    TEXT_SECONDARY,
    CHECKBOX_BORDER,
    CHECKBOX_FILL,
    CHECKBOX_HOVER,
    CHECKBOX_CHECKMARK,
)


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
            "Count cigarette inventory",
            "File completed store closing paperwork",
            "Organize paperwork for office workflow",
        ),
    ),
    (
        "Patient status updates",
        (
            "Process new admissions in Access",
            "Process discharges in Access",
            "Update patient phases as needed",
            "Confirm phase 2 patients are excluded from store tracking",
        ),
    ),
    (
        "Deposit preparation",
        (
            "Create daily deposit sheet",
            "Review deposit sheet for accuracy",
            "Confirm deposit sheet matches collected envelopes",
        ),
    ),
    (
        "Store list generation",
        (
            "Generate today's store list",
            "Enter store book totals into Spent At Store column",
            "Enter petty cash quarters into Quarters column",
            "Enter eligible deposit additions",
            "Apply weekly $100 allowance cap",
            "Run Thursday replenishment if applicable",
        ),
    ),
    (
        "Withdrawal preparation",
        (
            "Generate withdrawals sheet from store list",
            "Add discharge-related withdrawals manually",
            "Add unusual manual withdrawals if needed",
            "Review withdrawals sheet for accuracy",
        ),
    ),
    (
        "Database transaction entry",
        (
            "Copy deposit values to Automated Deposits sheet",
            "Run add deposits script",
            "Copy withdrawal values to Automated Withdrawals sheet",
            "Run add withdrawals script",
        ),
    ),
    (
        "Final balancing",
        (
            "Open Client Trust Balance sheet",
            "Verify deposits and withdrawals updated correctly",
            "Check for negative balances",
            "Confirm trust total balances",
            "Print new store list",
            "Send store list to campus store",
        ),
    ),
)


class ChecklistPage(ctk.CTkFrame):
    """
    Main dashboard page for the daily workflow checklist.
    """

    def __init__(self, parent):
        super().__init__(parent, fg_color=COLOR_BG_MAIN)

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.title_label = ctk.CTkLabel(
            self,
            text="DAILY CHECKLIST",
            text_color=TEXT_PRIMARY,
        )

        self.title_label.grid(
            row=0,
            column=0,
            padx=25,
            pady=(20, 10),
            sticky="w"
        )

        self.content_frame = ctk.CTkFrame(
            self,
            fg_color="transparent"
        )

        self.content_frame.grid(
            row=1,
            column=0,
            sticky="nsew",
            padx=20,
            pady=(0, 20)
        )

        self.content_frame.grid_columnconfigure(0, weight=1)
        self.content_frame.grid_rowconfigure(0, weight=1)

        self.scrollable_frame = ctk.CTkScrollableFrame(
            self.content_frame,
            fg_color="transparent"
        )

        self.scrollable_frame.grid(
            row=0,
            column=0,
            sticky="nsew"
        )

        self.scrollable_frame.grid_columnconfigure(0, weight=1)

        self.sections_container = ctk.CTkFrame(
            self.scrollable_frame,
            fg_color="transparent"
        )

        self.sections_container.grid(
            row=0,
            column=0,
            sticky="nsew",
            padx=5,
            pady=5
        )

        self.sections_container.grid_columnconfigure(0, weight=1)

        self.section_cards = []

        for title, tasks in CHECKLIST_SECTIONS:
            card = self.create_section_card(
                self.sections_container,
                title,
                tasks
            )

            self.section_cards.append(card)

        self.layout_cards()

    def create_section_card(self, parent, title, tasks):
        card = ctk.CTkFrame(
            parent,
            corner_radius=12,
            fg_color=CARD_BG,
            border_width=1,
            border_color=CARD_BORDER,
        )

        card.grid_columnconfigure(0, weight=1)

        title_label = ctk.CTkLabel(
            card,
            text=title,
            text_color=TEXT_PRIMARY,
        )

        title_label.grid(
            row=0,
            column=0,
            padx=15,
            pady=(15, 10),
            sticky="w"
        )

        for index, task in enumerate(tasks, start=1):
            checkbox = ctk.CTkCheckBox(
                card,
                text=task,
                text_color=TEXT_SECONDARY,
                fg_color=CHECKBOX_FILL,
                hover_color=CHECKBOX_HOVER,
                border_color=CHECKBOX_BORDER,
                checkmark_color=CHECKBOX_CHECKMARK,
            )

            checkbox.grid(
                row=index,
                column=0,
                padx=15,
                pady=(0, 10),
                sticky="w"
            )

        return card

    def layout_cards(self):
        columns = 2

        for index, card in enumerate(self.section_cards):
            row = index // columns
            column = index % columns

            self.sections_container.grid_columnconfigure(
                column,
                weight=1,
                uniform="checklist_cards"
            )

            card.grid(
                row=row,
                column=column,
                sticky="nsew",
                padx=10,
                pady=10
            )