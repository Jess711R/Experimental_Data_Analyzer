import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA

class Visualizer:
    """
    Contains plotting functions for experimental data.
    """

    def __init__(self):
        # Use a clean seaborn theme
        sns.set(style="whitegrid")

    def line_plot(self, df: pd.DataFrame, x: str, y: str, title=None):
        """
        Draws a line plot with markers.
        """
        plt.figure(figsize=(6, 4))
        sns.lineplot(data=df, x=x, y=y, marker="o")
        plt.title(title or f"{y} over {x}")
        plt.tight_layout()
        plt.show()

    def bar_plot(self, df: pd.DataFrame, x: str, y: str, title=None):
        """
        Draws a simple bar plot.
        """
        plt.figure(figsize=(6, 4))
        sns.barplot(data=df, x=x, y=y)
        plt.title(title or f"{y} by {x}")
        plt.tight_layout()
        plt.show()

    def heatmap(self, df: pd.DataFrame, title="Correlation Heatmap"):
        """
        Generates a correlation heatmap.
        """
        corr = df.corr(numeric_only=True)

        plt.figure(figsize=(6, 4))
        sns.heatmap(corr, annot=True, cmap="viridis", fmt=".2f")
        plt.title(title)
        plt.tight_layout()
        plt.show()

    def scatter_plot(self, df: pd.DataFrame, x: str, y: str, hue=None, title=None):
        """
        Quick scatter plot.
        """
        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=df, x=x, y=y, hue=hue)
        plt.title(title or f"{y} vs {x}")
        plt.tight_layout()
        plt.show()

    def pca_plot(self, df: pd.DataFrame, title="PCA Plot"):
        """
        Runs PCA on numeric columns and shows a 2D scatter plot.
        """
        numeric_df = df.select_dtypes(include="number").dropna()

        if numeric_df.shape[1] < 2:
            raise ValueError("PCA requires at least 2 numeric columns.")

        pca = PCA(n_components=2)
        pca_result = pca.fit_transform(numeric_df)

        # Create a temporary plotting DataFrame
        plot_df = pd.DataFrame({
            "PC1": pca_result[:, 0],
            "PC2": pca_result[:, 1]
        })

        plt.figure(figsize=(6, 4))
        sns.scatterplot(data=plot_df, x="PC1", y="PC2")
        plt.title(title)
        plt.tight_layout()
        plt.show()
