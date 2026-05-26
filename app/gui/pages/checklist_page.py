"""
Checklist page.
Displays the default home view for the daily workflow checklist.
"""

import customtkinter as ctk
from app.gui.theme import COLOR_BG_MAIN


class ChecklistPage(ctk.CTkFrame):

    """
    Main dashboard page for the daily workflow checklist.
    """

    def __init__(self, parent):

        super().__init__(parent, fg_color=COLOR_BG_MAIN)

        ctk.CTkLabel(
            self,
            text="DAILY CHECKLIST",
        ).pack(padx=25, pady=20, anchor="w")