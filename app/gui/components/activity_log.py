from datetime import datetime

import customtkinter as ctk

from app.gui.theme import COLOR_BG_LOG, COLOR_BG_MAIN, TEXT_MUTED


class ActivityLog(ctk.CTkFrame):
    """
    Bottom application log panel.
    """

    def __init__(self, parent):
        super().__init__(parent, height=130, fg_color=COLOR_BG_LOG)

        self.text_area = ctk.CTkTextbox(
            self,
            wrap="word",
            state="disabled",
            fg_color=COLOR_BG_MAIN,
            text_color=TEXT_MUTED,
        )
        self.text_area.pack(fill="both", expand=True, padx=10, pady=10)

    def log_message(self, message: str) -> None:
        """
        Add a timestamped message to the activity log.
        """

        timestamp = datetime.now().strftime("%I:%M:%S %p")
        log_entry = f"[{timestamp}] {message}"

        self.text_area.configure(state="normal")
        self.text_area.insert("end", log_entry + "\n")
        self.text_area.configure(state="disabled")
        self.text_area.see("end")