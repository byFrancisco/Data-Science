#utilizamos el mismo pero lo visualizamos mas detallado 
import pandas as pd

import seaborn as sns 
import matplotlib.pyplot as plt


full_health_data = pd.read_csv("Math/data8.csv", header=0, sep=",")
correlation_full_health = full_health_data.corr()

axis_corr = sns.heatmap(
correlation_full_health,
vmin=-1, vmax=1, center=0,
cmap=sns.diverging_palette(50, 500, n=500),
square=True
)

plt.show(block= True)

