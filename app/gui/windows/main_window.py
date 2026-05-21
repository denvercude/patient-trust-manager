"""
Main application window.

Defines the primary desktop window and arranges the major
application layout regions: topbar, sidebar, main content, and log.
"""

import customtkinter as ctk

from app.gui.components.topbar import Topbar
from app.gui.components.sidebar import Sidebar
from app.gui.components.activity_log import ActivityLog
from app.gui.pages.checklist_page import ChecklistPage


class MainWindow(ctk.CTk):
    """
    Root application window for Patient Trust Manager.
    """

    def __init__(self):
        super().__init__()

        # Set the default window size (width x height).
        self.geometry("1200x800")

        # Set the title displayed in the window header.
        self.title("")

        # Create the main components of the application.
        self.topbar = Topbar(self)
        self.sidebar = Sidebar(self)
        self.main_content = ctk.CTkFrame(self, fg_color="#1a1d24")
        self.bottom_log = ActivityLog(self)

        # Pack the components into the application window.
        self.topbar.pack(side="top", fill="x")
        self.bottom_log.pack(side="bottom", fill="x")
        self.sidebar.pack(side="left", fill="y")
        self.main_content.pack(side="right", fill="both", expand=True)

        # Prevent fixed-size components from changing size based on content.
        self.topbar.pack_propagate(False)
        self.sidebar.pack_propagate(False)
        self.bottom_log.pack_propagate(False)

        # Load the default page into the main content area.
        self.checklist_page = ChecklistPage(self.main_content)
        self.checklist_page.pack(fill="both", expand=True)