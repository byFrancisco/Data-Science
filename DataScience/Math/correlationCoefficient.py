#Three lines to make our compiler able to draw:
import sys
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

full_health_data=pd.read_csv("Math/data7.csv ", header=0,sep=",")

full_health_data.plot(x='Duracion',y='pulso maximo', kind='scatter')
plt.show(block=True)


#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()