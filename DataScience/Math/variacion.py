#Usamos python para encontrar la variacion
import pandas as pd
import numpy as np

health_data = pd.read_csv("Math/data4.csv", header=0, sep=",")
var = np.var(health_data)
print(var)