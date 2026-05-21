"""
Patient Trust Manager
Main application entry point.

Initializes the CustomTkinter application window and
applies global appearance settings.
"""

import customtkinter as ctk

from app.gui.windows.main_window import MainWindow


def main() -> None:
    """
    Configure global CustomTkinter settings and start the application.

    Keeping startup logic inside main() prevents the GUI from launching
    automatically if this file is imported by another module or test.
    """
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")

    app = MainWindow()
    app.mainloop()


if __name__ == "__main__":
    main()