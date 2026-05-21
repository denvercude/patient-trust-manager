"""
Activity log component.

Displays workflow messages, status updates, and future script output
at the bottom of the application window.
"""

import customtkinter as ctk


class ActivityLog(ctk.CTkFrame):
    """
    Bottom application log panel.
    """

    def __init__(self, parent):
        super().__init__(parent, height=130, fg_color="#0a0f1a")

        # Add a temporary heading to the activity log area.
        ctk.CTkLabel(
            self,
            text="ACTIVITY LOG"
        ).pack(padx=20, pady=10, anchor="w")