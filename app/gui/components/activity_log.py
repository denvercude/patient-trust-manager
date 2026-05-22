"""
Activity log component.

Displays workflow messages, status updates, and future script output
at the bottom of the application window.
"""

import customtkinter as ctk
from datetime import datetime


class ActivityLog(ctk.CTkFrame):
    """
    Bottom application log panel.
    """

    def __init__(self, parent):
        super().__init__(parent, height=130, fg_color="#0a0f1a")

        self.text_area = ctk.CTkTextbox(
            self,
            wrap="word",
            state="disabled",
        )
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)
    
    def log_message(self, message: str) -> None:
        """
        Add a timestamped message to the activity log.
        """

        timestamp = datetime.now().strftime("%I:%M:%S %p")
        log_message = f"[{timestamp}] {message}"

        self.text_area.configure(state="normal")
        self.text_area.insert("end", log_message + "\n")
        self.text_area.configure(state="disabled")
        self.text_area.see("end")


