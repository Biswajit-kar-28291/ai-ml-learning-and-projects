import os
import matplotlib.pyplot as plt
import seaborn as sns
from .config import CHARTS_FOLDER


class DataVisualizer:
    def __init__(self, data):
        self.data = data
        os.makedirs(CHARTS_FOLDER, exist_ok=True)
        sns.set_style("whitegrid")

    def plot_item_type_distribution(self):
        """Plot top item type distribution"""
        plt.figure(figsize=(12, 6))
        self.data["item_type"].value_counts().plot(kind="bar")
        plt.title("Item Type Distribution")
        plt.xlabel("Item Type")
        plt.ylabel("Count")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/item_type_distribution.png")
        plt.close()

    def plot_fat_content_distribution(self):
        """Plot item fat content distribution"""
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.data, x="item_fat_content")
        plt.title("Item Fat Content Distribution")
        plt.xlabel("Fat Content")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/fat_content_distribution.png")
        plt.close()

    def plot_outlet_type_distribution(self):
        """Plot outlet type distribution"""
        plt.figure(figsize=(10, 6))
        self.data["outlet_type"].value_counts().plot(kind="bar")
        plt.title("Outlet Type Distribution")
        plt.xlabel("Outlet Type")
        plt.ylabel("Count")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/outlet_type_distribution.png")
        plt.close()

    def plot_outlet_location_distribution(self):
        """Plot outlet location type distribution"""
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.data, x="outlet_location_type")
        plt.title("Outlet Location Type Distribution")
        plt.xlabel("Outlet Location Type")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/outlet_location_distribution.png")
        plt.close()

    def plot_average_mrp_by_item_type(self):
        """Plot average MRP by item type"""
        avg_mrp = self.data.groupby("item_type")["item_mrp"].mean().sort_values(ascending=False)

        plt.figure(figsize=(12, 6))
        avg_mrp.plot(kind="bar")
        plt.title("Average MRP by Item Type")
        plt.xlabel("Item Type")
        plt.ylabel("Average MRP")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/average_mrp_by_item_type.png")
        plt.close()

    def plot_average_mrp_by_outlet_type(self):
        """Plot average MRP by outlet type"""
        avg_mrp = self.data.groupby("outlet_type")["item_mrp"].mean().sort_values(ascending=False)

        plt.figure(figsize=(10, 6))
        avg_mrp.plot(kind="bar")
        plt.title("Average MRP by Outlet Type")
        plt.xlabel("Outlet Type")
        plt.ylabel("Average MRP")
        plt.xticks(rotation=30, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/average_mrp_by_outlet_type.png")
        plt.close()

    def plot_visibility_by_item_type(self):
        """Plot average visibility by item type"""
        avg_visibility = self.data.groupby("item_type")["item_visibility"].mean().sort_values(ascending=False)

        plt.figure(figsize=(12, 6))
        avg_visibility.plot(kind="bar")
        plt.title("Average Item Visibility by Item Type")
        plt.xlabel("Item Type")
        plt.ylabel("Average Visibility")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/visibility_by_item_type.png")
        plt.close()

    def plot_outlet_size_distribution(self):
        """Plot outlet size distribution"""
        plt.figure(figsize=(8, 5))
        sns.countplot(data=self.data, x="outlet_size")
        plt.title("Outlet Size Distribution")
        plt.xlabel("Outlet Size")
        plt.ylabel("Count")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/outlet_size_distribution.png")
        plt.close()

    def generate_all_charts(self):
        """Generate all charts"""
        print("Generating charts...")

        self.plot_item_type_distribution()
        self.plot_fat_content_distribution()
        self.plot_outlet_type_distribution()
        self.plot_outlet_location_distribution()
        self.plot_average_mrp_by_item_type()
        self.plot_average_mrp_by_outlet_type()
        self.plot_visibility_by_item_type()
        self.plot_outlet_size_distribution()

        print(f"All charts saved in: {CHARTS_FOLDER}")