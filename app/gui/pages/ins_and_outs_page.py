"""
Ins and Outs page.
"""

import customtkinter as ctk

from app.gui.theme import COLOR_BG_MAIN


class InsAndOutsPage(ctk.CTkFrame):

    def __init__(self, parent):
        super().__init__(
            parent,
            fg_color=COLOR_BG_MAIN
        )

        label = ctk.CTkLabel(
            self,
            text="INS AND OUTS PAGE"
        )

        label.pack(
            padx=20,
            pady=20
        )