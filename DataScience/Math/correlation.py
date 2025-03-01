#Three lines to make our compiler able to draw
import sys 
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

health_data = pd.read_csv("Math/data6.csv ", header=0, sep=",")
#agregamos el nombre de los datos
#solo funciona de acuerdo a los datos csv 
health_data.plot(x = "Average_Pulse", y='Calorie_Burnage', kind='scatter'),
plt.show(block=True)

#Two lines to make our compiler able to draw
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()