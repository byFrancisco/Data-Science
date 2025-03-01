import sys 
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
plt.ion() #Activamos la interactividad

health_data = pd.read_csv("data.csv", header=0, sep=",")

health_data.plot(x ='Average_Pulse', y='Calorie_Burnage', kind='line')
plt.ylim(ymin=0)
plt.xlim(xmin=0)

plt.show(block=True)

#dos lineas se crean en nuestro compilador a dibujar
plt.savefig(sys.stdout.buffer)
sys.stdout.flush