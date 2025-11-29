import pandas as pd
import os

class DataLoader:
    """
    Loads CSV or Excel files and validates required columns.
    """

    def __init__(self, required_columns=None):
        """
        required_columns: list of column names the dataset must include.
        """
        self.required_columns = required_columns or []

    def load(self, filepath: str) -> pd.DataFrame:
        """
        Loads a CSV or Excel file into a pandas DataFrame.
        Includes robust handling for Windows encodings.
        """
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File not found: {filepath}")

        ext = filepath.lower().split(".")[-1]

        try:
            if ext == "csv":
                # Try UTF-8 first, fallback to latin1 (Windows Excel encoding)
                try:
                    df = pd.read_csv(filepath, encoding="utf-8")
                except UnicodeDecodeError:
                    df = pd.read_csv(filepath, encoding="latin1")

            elif ext in ["xlsx", "xls"]:
                df = pd.read_excel(filepath)

            else:
                raise ValueError("Unsupported file type. Use CSV or Excel files.")

            if df.empty:
                raise ValueError("Loaded file is empty.")

            return df

        except Exception as e:
            raise RuntimeError(f"Error loading file: {e}")
