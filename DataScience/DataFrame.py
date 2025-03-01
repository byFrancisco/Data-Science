#Creaamos un data frame con pandas
#data frame es una estructura de represenatacion de datos

import pandas as pd

d = {'col1':[1,2,3,4,7], 'col2': [4,5,6,9,5], 'col3':[7,8,12,1,11]}

df = pd.DataFrame(data=d)
#si solo queremos ver una columna
count_colum = df.shape[1]
#O si queremos mostrar el numero de rows
count_row = df.shape[0]

print("Number of columns: ")
print(count_colum)
print("Number of rows:")
print(count_row)
print(df)