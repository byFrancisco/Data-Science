#Usamos la variacion para encontrar el conjunto de datos completos 
import pandas as pd
import numpy as np

full_health_data = pd.read_csv("Math/data5.csv ", header=0,sep=",")

var =np.var(full_health_data)
print(var)