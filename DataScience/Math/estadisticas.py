#Describimos las estadisticas resumiendo lo mas importante de los datos
#Data science
import pandas as pd

full_health_data = pd.read_csv("Math/data_.csv", header=0, sep=",")

pd.set_option('display.max_columns',None)
pd.set_option('display.max_rows',None)

print(full_health_data.describe())