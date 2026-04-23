import pandas as pd 
import os
from .config import RAW_DATA_PATH

class Dataloader:
    def __init__(self, file_path=RAW_DATA_PATH):
        self.file_path=file_path
    
    def load_data(self):
        """Load dataset from csv file"""
        if not os.path.exists(self.file_path):
            return FileNotFoundError(f"file not found at {self.file_path}")
        data=pd.read_csv(self.file_path)
        print("Data lodeade successfully")
        return data
    
    def show_basic_info(self, data):
        """Display basic info"""
        print("first five row")
        print(data.head())

        print("collumn")
        print(data.columns.tolist())
