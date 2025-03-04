import sys
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

full_health_data = pd.read_csv("Math/DSAVANCED/datos.csv", header= 0, sep=",")

x=full_health_data["Average_Pulse"]
y=full_health_data["Calorie_Burnage"]

slope,intercept, r,p, strd_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x, y)
plt.plot(x, mymodel)
plt.ylim(ymin =0, ymax=2000)
plt.xlim(xmin= 0, xmax=200)
plt.xlabel( "Average_Pulse")
plt.ylabel("Calorie_Burnage")
plt.show(block=True)

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()