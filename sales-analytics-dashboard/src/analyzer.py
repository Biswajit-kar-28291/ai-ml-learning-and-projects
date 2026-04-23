import pandas as pd


class SalesAnalyzer:
    def __init__(self, data):
        self.data = data

    def total_items(self):
        """Return total number of items"""
        return len(self.data)

    def average_item_mrp(self):
        """Return average MRP of items"""
        return round(self.data["item_mrp"].mean(), 2)

    def max_item_mrp(self):
        """Return maximum item MRP"""
        return round(self.data["item_mrp"].max(), 2)

    def min_item_mrp(self):
        """Return minimum item MRP"""
        return round(self.data["item_mrp"].min(), 2)

    def average_item_weight(self):
        """Return average item weight"""
        return round(self.data["item_weight"].mean(), 2)

    def item_type_distribution(self):
        """Return count of each item type"""
        return self.data["item_type"].value_counts()

    def fat_content_distribution(self):
        """Return count of each fat content category"""
        return self.data["item_fat_content"].value_counts()

    def outlet_type_distribution(self):
        """Return count of each outlet type"""
        return self.data["outlet_type"].value_counts()

    def outlet_size_distribution(self):
        """Return count of each outlet size"""
        return self.data["outlet_size"].value_counts(dropna=False)

    def outlet_location_distribution(self):
        """Return count of each outlet location type"""
        return self.data["outlet_location_type"].value_counts()

    def average_mrp_by_item_type(self):
        """Return average MRP grouped by item type"""
        return self.data.groupby("item_type")["item_mrp"].mean().sort_values(ascending=False)

    def average_mrp_by_outlet_type(self):
        """Return average MRP grouped by outlet type"""
        return self.data.groupby("outlet_type")["item_mrp"].mean().sort_values(ascending=False)

    def average_visibility_by_item_type(self):
        """Return average visibility grouped by item type"""
        return self.data.groupby("item_type")["item_visibility"].mean().sort_values(ascending=False)

    def outlet_age(self):
        """Create outlet age column"""
        current_year = pd.Timestamp.now().year
        self.data["outlet_age"] = current_year - self.data["outlet_establishment_year"]
        return self.data

    def average_mrp_by_outlet_age(self):
        """Return average MRP by outlet age"""
        self.outlet_age()
        return self.data.groupby("outlet_age")["item_mrp"].mean().sort_index()

    def top_expensive_items(self, n=10):
        """Return top n most expensive items"""
        return self.data[["item_identifier", "item_type", "item_mrp"]].sort_values(
            by="item_mrp", ascending=False
        ).head(n)

    def summary_kpis(self):
        """Return key summary metrics as dictionary"""
        return {
            "Total Items": self.total_items(),
            "Average Item MRP": self.average_item_mrp(),
            "Maximum Item MRP": self.max_item_mrp(),
            "Minimum Item MRP": self.min_item_mrp(),
            "Average Item Weight": self.average_item_weight()
        }