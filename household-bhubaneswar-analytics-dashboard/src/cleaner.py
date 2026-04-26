import pandas as pd
import numpy as np
import os
from .config import PROCESSED_DATA_PATH

class Datacleaner:
    def __init__(self):
        pass

    def std_cl_name(self,data):
        data.columns=(
            data.columns.str.strip()
            .str.lower()
            .str.replace(" ","_")
            .str.replace(".","")
        )
        print("column stndard")
        return data
    def rm_duplicate(self, data):
        prev=data.shape[0]
        data=data.drop_duplicates()
        now=data.shape[0]
        print(f"total {prev-now} row remove")
        return data
    
    def handel_null(self, data):
        data["ward_name"]=data["ward_name"].astype(str)
        data["ward_no"]=data["ward_no"].str.replace("W","").astype(int)
        num_col=data.select_dtypes(include=[np.number]).columns
        ob_col=data.select_dtypes(include=["object"]).columns
       
        for col in num_col:
            data[col]=data[col].fillna(data[col].mean())
        for col in ob_col:
            data[col]=data[col].fillna("unknow")
        print(num_col)
        print(ob_col)
        return data
    
    def save_value(slef,data):
        os.makedirs(os.path.dirname(PROCESSED_DATA_PATH),exist_ok=True)
        data.to_csv(PROCESSED_DATA_PATH, index=False)
        print(f"Cleaned data saved to: {PROCESSED_DATA_PATH}")


    def cleaned_data(self,data):
        data=self.std_cl_name(data)
        data=self.rm_duplicate(data)
        data=self.handel_null(data)
        return data
