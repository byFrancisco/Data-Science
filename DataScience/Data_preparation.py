import pandas as pd
#nombramos data frame como health_data
health_data = pd.read_csv("data.csv ", header = 0, sep=",")
#si removemos los Nan cells, limpiara los datos y pueden ser analizados 
#health_data.dropna(axis=0,inplace=True)
pd.set_option('display.max_columns',None)
#si utilizamos el head, parara las funciones en el 5 rows
print(health_data)

#calculamos y analizamos los datos, convertimos el 
# tipo objeto a float64(es un numero decimal con python)
print(health_data.info())

#describimos y mostramos 
print(health_data.describe())
