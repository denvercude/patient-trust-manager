"""
Patient Trust Manager
Main application entry point.

Initializes the CustomTkinter application window and
applies global appearance settings.
"""

import customtkinter as ctk

from app.gui.windows.main_window import MainWindow


# -------------------------------------------------------------------
# Global application styling
# -------------------------------------------------------------------

# Set the application appearance mode.
# Options: "light", "dark", "system"
ctk.set_appearance_mode("dark")

# Set the default widget color theme.
# Available built-in themes include:
# "blue", "green", and "dark-blue"
ctk.set_default_color_theme("dark-blue")


# -------------------------------------------------------------------
# Application startup
# -------------------------------------------------------------------

# Create and start the main application window.
app = MainWindow()
app.mainloop()