import pandas as pd 

class analyzer:
    def __init__(self):
        pass

    def total_households_in_city(self,data):
        return (data['total_no_of_households'].sum())
    
    def zone_wise_analysis(self,data):

        d=data.groupby("zone_name")["total_no_of_households"].sum()
        return ({
    "highest": {"zone": d.idxmax(), "households": d.max()},
    "lowest": {"zone": d.idxmin(), "households": d.min()}
    })

    def word_wise_analysis(self,data):

        d=data.groupby("ward_no")["total_no_of_households"].sum()

        data=d.sort_values(ascending=False)

        return {
        "top_5_wards": data.head(5).to_dict(),
        "bottom_5_wards":data.tail(5).to_dict(),
        "most_populated_ward": {
            "ward_name":  d.idxmax(),
            "households": d.max()
        }
    }

    def average_households_per_ward(self,data):

        d=data.groupby("ward_no")["total_no_of_households"].mean()

        return {
        "average_households_per_ward":d.to_dict()
    }

    def outlier_detection(self, data):
        d = data.groupby("ward_name")["total_no_of_households"].sum()

        mean = d.mean()
        std = d.std()

        upper_limit = mean + 2 * std
        lower_limit = mean - 2 * std

        high_outliers = d[d > upper_limit]
        low_outliers = d[d < lower_limit]

        return {
            "high_outliers": high_outliers.to_dict(),
            "low_outliers": low_outliers.to_dict(),
            "mean": mean,
            "std_dev": std
        }
    
    def summary_kpis(self, data):
        return {
            "total_households_in_city": self.total_households_in_city(data),
            "zone_wise_analysis": self.zone_wise_analysis(data),
            "word_wise_analysis": self.word_wise_analysis(data),
            "average_households_per_ward": self.average_households_per_ward(data),
            "outlier_detection": self.outlier_detection(data)
        }

