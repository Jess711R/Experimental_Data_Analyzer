import tkinter as tk
from tkinter import filedialog, messagebox, ttk

from data_loader import DataLoader
from data_manager import DataManager
from visualizer import Visualizer

import pandas as pd

class App(tk.Tk):
    """
    Tkinter GUI for the Experimental Data Analyzer.
    Handles file upload, filtering, and visualization.
    """

    def __init__(self):
        super().__init__()

        self.title("Experimental Data Analyzer")
        self.geometry("650x550")
        self.resizable(False, False)

        # Core objects
        self.loader = DataLoader()
        self.visualizer = Visualizer()
        self.df = None  # will store the loaded DataFrame

        # --- GUI LAYOUT ---
        self._build_ui()

    def _build_ui(self):
        """
        Creates all GUI widgets (buttons, dropdowns, etc.)
        """

        # Upload section
        upload_frame = tk.LabelFrame(self, text="1. Upload Data File")
        upload_frame.pack(fill="x", padx=15, pady=10)

        tk.Button(upload_frame, text="Select File", command=self.upload_file).pack(pady=5)

        self.file_label = tk.Label(upload_frame, text="No file selected.")
        self.file_label.pack()

        # Filtering section
        filter_frame = tk.LabelFrame(self, text="2. Filter Data")
        filter_frame.pack(fill="x", padx=15, pady=10)

        tk.Label(filter_frame, text="Column:").grid(row=0, column=0, padx=5, pady=5)
        self.filter_col_entry = tk.Entry(filter_frame)
        self.filter_col_entry.grid(row=0, column=1, padx=5)

        tk.Label(filter_frame, text="Value:").grid(row=0, column=2, padx=5)
        self.filter_val_entry = tk.Entry(filter_frame)
        self.filter_val_entry.grid(row=0, column=3, padx=5)

        tk.Button(filter_frame, text="Apply Filter", command=self.apply_filter).grid(row=0, column=4, padx=10)

        # Plotting section
        plot_frame = tk.LabelFrame(self, text="3. Plotting")
        plot_frame.pack(fill="both", expand=True, padx=15, pady=10)

        tk.Label(plot_frame, text="Plot Type:").grid(row=0, column=0, padx=5, pady=5)

        self.plot_type = tk.StringVar()
        plot_options = ["Line Plot", "Bar Plot", "Scatter Plot", "Heatmap", "PCA"]
        self.plot_dropdown = ttk.Combobox(plot_frame, textvariable=self.plot_type, values=plot_options, state="readonly")
        self.plot_dropdown.grid(row=0, column=1, padx=5)
        self.plot_dropdown.set("Line Plot")

        tk.Label(plot_frame, text="X-axis:").grid(row=1, column=0, padx=5)
        self.x_entry = tk.Entry(plot_frame)
        self.x_entry.grid(row=1, column=1, padx=5)

        tk.Label(plot_frame, text="Y-axis:").grid(row=2, column=0, padx=5)
        self.y_entry = tk.Entry(plot_frame)
        self.y_entry.grid(row=2, column=1, padx=5)

        tk.Button(plot_frame, text="Generate Plot", command=self.generate_plot).grid(row=3, column=0, columnspan=2, pady=15)

    # =============================
    # BUTTON FUNCTIONS
    # =============================

    def upload_file(self):
        filepath = filedialog.askopenfilename(
            title="Select CSV or Excel file",
            filetypes=[("CSV files", "*.csv"), ("Excel files", "*.xlsx *.xls")]
        )

        if not filepath:
            return

        try:
            self.df = self.loader.load(filepath)
            self.file_label.config(text=f"Loaded: {filepath.split('/')[-1]}")
            messagebox.showinfo("Success", "File loaded successfully!")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def apply_filter(self):
        """
        Applies a simple filter: column == value
        """
        if self.df is None:
            messagebox.showerror("Error", "Please upload a dataset first.")
            return

        col = self.filter_col_entry.get().strip()
        val = self.filter_val_entry.get().strip()

        if not col or not val:
            messagebox.showerror("Error", "Please enter both column and value.")
            return

        try:
            manager = DataManager(self.df)
            filtered = manager.filter(**{col: val})

            if filtered.empty:
                messagebox.showwarning("No Data", "No rows match the filter.")
            else:
                self.df = filtered
                messagebox.showinfo("Success", f"Filter applied. {len(filtered)} rows remaining.")

        except Exception as e:
            messagebox.showerror("Error", str(e))

    def generate_plot(self):
        """
        Uses the selected plot type and creates the visualization.
        """
        if self.df is None:
            messagebox.showerror("Error", "Upload a dataset before plotting.")
            return

        plot_type = self.plot_type.get()

        try:
            if plot_type == "Line Plot":
                self.visualizer.line_plot(self.df, self.x_entry.get(), self.y_entry.get())

            elif plot_type == "Bar Plot":
                self.visualizer.bar_plot(self.df, self.x_entry.get(), self.y_entry.get())

            elif plot_type == "Scatter Plot":
                self.visualizer.scatter_plot(self.df, self.x_entry.get(), self.y_entry.get())

            elif plot_type == "Heatmap":
                self.visualizer.heatmap(self.df)

            elif plot_type == "PCA":
                self.visualizer.pca_plot(self.df)

        except Exception as e:
            messagebox.showerror("Plot Error", str(e))
