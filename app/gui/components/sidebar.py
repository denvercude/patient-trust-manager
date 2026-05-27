"""
Sidebar component.

Displays the left navigation area for workflow pages and extra tools.
"""

import customtkinter as ctk
from app.gui.theme import COLOR_BG_SIDE

class Sidebar(ctk.CTkFrame):
    """
    Left navigation sidebar of the application.
    """

    def __init__(self, parent, on_nav_click):
        super().__init__(parent, width=220, fg_color=COLOR_BG_SIDE)

        self.on_nav_click = on_nav_click

        self.workflow_label = ctk.CTkLabel(
            self,
            text="WORKFLOW",
        )

        self.workflow_label.pack(
            anchor="w",
            padx=15,
            pady=(20, 8)
        )

        self.workflow_button = ctk.CTkButton(
            self,
            text="Home / Checklist",
            anchor="w",
            height=34,
            corner_radius=6,
            border_width=0,
            fg_color="transparent",
            hover_color="#17365C",
            command=lambda: [
                self.set_active_button(self.workflow_button),
                self.on_nav_click("workflow")
            ],
        )

        self.workflow_button.pack(
            fill="x",
            padx=8,
            pady=2
        )

        self.ins_and_outs_button = ctk.CTkButton(
            self,
            text="Ins and Outs",
            anchor="w",
            height=34,
            corner_radius=6,
            border_width=0,
            fg_color="transparent",
            hover_color="#17365C",
            command=lambda: [
                self.set_active_button(self.ins_and_outs_button),
                self.on_nav_click("ins_and_outs")
            ],
        )

        self.ins_and_outs_button.pack(
            fill="x",
            padx=8,
            pady=2,
        )

        self.set_active_button(self.workflow_button)
    
    def set_active_button(self, active_button):

        buttons = [
            self.workflow_button,
            self.ins_and_outs_button,
        ]

        for button in buttons:
            button.configure(fg_color="transparent")

        active_button.configure(fg_color="#17365C")