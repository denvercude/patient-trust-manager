"""
Sidebar component.

Displays the left navigation area for workflow pages and extra tools.
"""

import customtkinter as ctk


class Sidebar(ctk.CTkFrame):
    """
    Left navigation sidebar of the application.
    """

    def __init__(self, parent):
        super().__init__(parent, width=220, fg_color="#111827")

        # Add a temporary section heading to the sidebar.
        ctk.CTkLabel(
            self,
            text="WORKFLOW"
        ).pack(padx=20, pady=(20, 10), anchor="w")