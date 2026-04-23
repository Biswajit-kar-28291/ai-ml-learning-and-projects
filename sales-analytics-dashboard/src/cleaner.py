import pandas as pd
import numpy as np
import os 
from .config import PROCESSED_DATA_PATH

class Deatacleaner:
    def __init__(self):
        pass

    def standardize_column_names(self, data):
        """Convert column names to clean snake_case format"""
        data.columns = (
            data.columns.str.strip()
            .str.lower()
            .str.replace(" ", "_")
            .str.replace("-", "_")
        )
        return data
    
    def remove_duplicates(self,data):
        """Remove duplicates row"""
        before=data.shape[0]
        data=data.drop_duplicates()
        after=data.shape[0]
        print(f"remove {before-after} duplicates row")
        return data
    
    def handel_missing_value(self,data):
        """Handel missing value"""
        numeric_columns=data.select_dtypes(include=[np.number]).columns
        categorical_coloumns=data.select_dtypes(include=["object"]).columns

        for column in numeric_columns:
            data[column]=data[column].fillna(data[column].mean())

        for column in categorical_coloumns:
            data[column]=data[column].fillna("Unknown")

        return data
    

    def save_cleaned_data(self, data):
        """Save cleaned data to processed folder"""
        os.makedirs(os.path.dirname(PROCESSED_DATA_PATH), exist_ok=True)
        data.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"Cleaned data saved to: {PROCESSED_DATA_PATH}")

    def clean_data(self, data):
        """Run full cleaning pipeline"""
        print("Starting data cleaning...")

        data = self.standardize_column_names(data)
        data = self.remove_duplicates(data)
        data = self.handel_missing_value(data)
        # data = self.convert_date_column(data)
        # data = self.create_derived_columns(data)

        print("Data cleaning completed")
        return data