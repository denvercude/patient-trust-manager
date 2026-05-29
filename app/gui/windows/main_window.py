"""
Main application window.

Defines the primary desktop window and arranges the major
application layout regions: topbar, sidebar, main content, and log.
"""

import tkinter as tk
import customtkinter as ctk

from app.gui.components.topbar import Topbar
from app.gui.components.sidebar import Sidebar
from app.gui.components.activity_log import ActivityLog
from app.gui.pages.checklist_page import ChecklistPage
from app.gui.pages.ins_and_outs_page import InsAndOutsPage
from app.gui.theme import COLOR_BG_MAIN


class MainWindow(ctk.CTk):
    """
    Root application window for Patient Trust Manager.
    """

    def __init__(self):
        super().__init__()

        # Set the default window size (width x height).
        self.geometry("1200x800")

        # Set the title displayed in the window header.
        self.title("Patient Trust Manager")

        # Create the application menu bar.
        self.menu_bar = tk.Menu(self)

        # Create the File menu.
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Exit", command=self.quit)

        # Create the Help menu.
        help_menu = tk.Menu(self.menu_bar, tearoff=0)
        help_menu.add_command(label="About", command=lambda: print("Patient Trust Manager"))

        # Add menus to the menu bar.
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        self.menu_bar.add_cascade(label="Help", menu=help_menu)

        # Attach the menu bar to the application window.
        self.config(menu=self.menu_bar)

        # Create the main components of the application.
        self.topbar = Topbar(self)
        self.sidebar = Sidebar(self, self.show_page)
        self.main_content = ctk.CTkFrame(self, fg_color=COLOR_BG_MAIN)
        self.activity_log = ActivityLog(self)

        # Track the current page.
        self.current_page = None

        # Pack the components into the application window.
        self.topbar.pack(side="top", fill="x")
        self.activity_log.pack(side="bottom", fill="x")
        self.sidebar.pack(side="left", fill="y")
        self.main_content.pack(side="left", fill="both", expand=True)

        # Prevent fixed-size components from changing size based on content.
        self.topbar.pack_propagate(False)
        self.sidebar.pack_propagate(False)
        self.activity_log.pack_propagate(False)
        
        # Log application startup to the activity log.
        self.activity_log.log_message("Application started")

        self.show_page("workflow")
    
    def show_page(self, page_name):
        """
        Load the selected page into the main content area.
        Ignore the request if the selected page is already active.
        """

        if self.current_page == page_name:
            return

        self.current_page = page_name

        for widget in self.main_content.winfo_children():
            widget.destroy()

        if page_name == "workflow":
            page = ChecklistPage(self.main_content)
            page.pack(fill="both", expand=True)
        elif page_name == "ins_and_outs":
            page = InsAndOutsPage(self.main_content)
            page.pack(fill="both", expand=True)