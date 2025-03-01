#Funcion matematica que tendra dificultades para predecir los valores
#precisos si las observaciones estan "dispersas" 
#verificaremos que rango es alto
import pandas as pd
import numpy as np

full_health_data = pd.read_csv("Math/data_.csv", header=0, sep=",")

cv=np.std(full_health_data) / np.mean(full_health_data)
print(cv)
