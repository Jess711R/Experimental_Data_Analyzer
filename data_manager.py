import pandas as pd

class DataManager:
    """
    Handles filtering, statistics, and data manipulation.
    """

    def __init__(self, df: pd.DataFrame = None):
        """
        Stores the DataFrame for further operations.
        df is optional at initialization since the user loads data later.
        """
        if df is not None and not isinstance(df, pd.DataFrame):
            raise TypeError("DataManager expects a pandas DataFrame or None.")
        
        self.df = df

    def set_dataframe(self, df: pd.DataFrame):
        """
        Updates the stored DataFrame after data is loaded from the GUI.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("set_dataframe expects a pandas DataFrame.")
        self.df = df

    def filter(self, **conditions):
        """
        Filters data based on user-specified column=value pairs.
        Example: filter(treatment="DrugA", dose=10)
        """
        if self.df is None:
            raise ValueError("No dataset loaded yet.")

        filtered = self.df.copy()

        for col, val in conditions.items():
            if col not in filtered.columns:
                raise KeyError(f"Column '{col}' not found in dataset.")
            filtered = filtered[filtered[col] == val]

        return filtered

    def stats(self, column: str):
        """
        Computes basic statistics for a given numeric column.
        Returns a dictionary with mean, std, min, max.
        """
        if self.df is None:
            raise ValueError("No dataset loaded yet.")

        if column not in self.df.columns:
            raise KeyError(f"Column '{column}' not found in dataset.")

        if not pd.api.types.is_numeric_dtype(self.df[column]):
            raise TypeError(f"Column '{column}' must be numeric to compute statistics.")

        series = self.df[column].dropna()

        return {
            "mean": float(series.mean()),
            "std": float(series.std()),
            "min": float(series.min()),
            "max": float(series.max())
        }

    def unique_values(self, column: str):
        """
        Returns unique values for a column (useful for dropdown menus).
        """
        if self.df is None:
            raise ValueError("No dataset loaded yet.")

        if column not in self.df.columns:
            raise KeyError(f"Column '{column}' not found.")
        
        return sorted(self.df[column].dropna().unique())
