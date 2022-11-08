import statistics
import pandas as pd
import csv
data1=pd.read_csv("medium_data.csv")
data2=data1["reading_time"].tolist()