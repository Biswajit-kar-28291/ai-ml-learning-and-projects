import os 
import matplotlib.pyplot as plt 
import seaborn as sns
from .config import CHARTS_FOLDER


class Datavisualizer:
    def __init__(self,data):
        self.data=data
        os.makedirs(CHARTS_FOLDER,exist_ok=True)

    def zone_wise_total_households(self):
        d=self.data.groupby("zone_name")["total_no_of_households"].sum()
        plt.figure(figsize=(8,5))
        d.plot(kind="bar")
        plt.title("Zone-wise Total Households")
        plt.xlabel("total_no_of_households")
        plt.ylabel("zone_name")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/zone_wise_total_households.png")
        plt.close()

    def ward_wise_household_distribution(self):
        d=self.data.nlargest(10, "total_no_of_households")
        plt.figure(figsize=(8,6))
        d.head(10).plot(kind="bar")
        plt.title("Zone-wise Total Households")
        plt.xlabel("zone_name")
        plt.ylabel("total_no_of_households")
        plt.xticks(rotation=45, ha="right")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/ward_wise_household_distribution.png")
        plt.close()

    
    def bottom_10_wards(self):
        bottom_wards = self.data.nsmallest(10, "total_no_of_households")

        plt.figure(figsize=(10, 6))
        sns.barplot(x="total_no_of_households", y="ward_no", data=bottom_wards, orient="h")
        plt.title("Bottom 10 Wards by Households")
        plt.xlabel("Total Households")
        plt.ylabel("Ward Number")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/bottom_10_wards.png")
        plt.close()

    def household_distribution(self):
        plt.figure(figsize=(12,6))
        sns.histplot(self.data['total_no_of_households'])
        plt.title("Household Distribution")
        plt.xlabel("Total Households")
        plt.ylabel("Frequency")
        plt.tight_layout()
        plt.savefig(f"{CHARTS_FOLDER}/bottom_10_wards.png")
        plt.close()
