import pandas as pd

class DataLoader:
    """
    Loads CSV or Excel files and validates required columns.
    """

    def __init__(self, required_columns=None):
        """
        required_columns: list of column names the dataset must include.
        """
        self.required_columns = required_columns or ["sample_id"]

    def load(self, filepath):
        """
        Loads a file based on its extension.
        """
        try:
            if filepath.endswith(".csv"):
                df = pd.read_csv(filepath)
            elif filepath.endswith(".xlsx") or filepath.endswith(".xls"):
                df = pd.read_excel(filepath)
            else:
                raise ValueError("Unsupported file type. Please upload CSV or Excel.")

            self._validate_columns(df)
            return df

        except Exception as e:
            raise RuntimeError(f"Error loading file: {e}")

    def _validate_columns(self, df):
        """
        Checks whether the required columns are present.
        """
        missing = [col for col in self.required_columns if col not in df.columns]
        if missing:
            raise ValueError(f"Missing required columns: {missing}")
