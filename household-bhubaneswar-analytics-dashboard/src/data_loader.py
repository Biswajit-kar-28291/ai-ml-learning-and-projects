import pandas as pd
import os 
from .config import RAW_DATA_PATH

class Dataloader:
    def __init__(self, file_path= RAW_DATA_PATH):
        self.file_path=RAW_DATA_PATH

    def loade_data(self):
        if not os.path.exists(self.file_path):
            return FileNotFoundError(f"file not found at {self.file_path}")
        data=pd.read_csv(self.file_path)
        print("data found")
        return data
    
    def show_data(self, data):
        print(data.head())

        print(data.columns.tolist())
        