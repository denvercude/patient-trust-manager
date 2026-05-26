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

    def __init__(self, parent):
        super().__init__(parent, width=500, fg_color=COLOR_BG_SIDE)

        # Add a temporary section heading to the sidebar.
        ctk.CTkLabel(
            self,
            text="WORKFLOW"
        ).pack(padx=20, pady=(20, 10), anchor="w")