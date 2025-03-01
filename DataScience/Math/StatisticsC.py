#Correlation Matrix in python
import pandas as pd

full_health_data = pd.read_csv("Math/data8.csv", header=0, sep=",")

Corr_Matrix = round(full_health_data.corr(),2)
print(Corr_Matrix)