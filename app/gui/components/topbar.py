"""
Topbar component.

Displays the application title and, eventually, connection status
indicators for Access, Excel, and required file paths.
"""

import customtkinter as ctk


class Topbar(ctk.CTkFrame):
    """
    Top horizontal header area of the application.
    """

    def __init__(self, parent):
        super().__init__(parent, height=70, fg_color="#0b1220")

        # Add the application title to the topbar.
        ctk.CTkLabel(
            self,
            text="CLIENT TRUST WORKFLOW"
        ).pack(padx=20, pady=20, anchor="w")