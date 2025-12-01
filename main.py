"""
main.py
Entry point for the Experimental Data Analyzer project.
Launches the Tkinter GUI and initializes all core modules.

Author: Your Name
"""

from gui import DataAnalyzerGUI
from data_loader import DataLoader
from data_manager import DataManager
from visualizer import Visualizer
import tkinter as tk
import traceback


def main():
    """
    Main program entry point.
    Initializes backend modules and starts the Tkinter GUI.
    """

    try:
        # Initialize backend components
        loader = DataLoader()
        manager = DataManager()
        visualizer = Visualizer()

        # Create the Tkinter root window
        root = tk.Tk()

        # Initialize the GUI and pass backend modules
        app = DataAnalyzerGUI(
            master=root,
            data_loader=loader,
            data_manager=manager,
            visualizer=visualizer
        )

        # Start the GUI event loop
        root.mainloop()

    except Exception as e:
        print("\n[ERROR] The application encountered an issue during startup.\n")
        print(type(e).__name__, ":", e)
        print("\nFull traceback:\n")
        traceback.print_exc()


if __name__ == "__main__":
    main()
