#Correlation Does Not Imply Causality
#Correlation measures the numerical relationship between two variables.
import sys
import matplotlib
matplotlib.use('TkAgg')

import pandas as pd
import matplotlib.pyplot as plt

Drowning_Accident = [20,40,60,80,100,120,140,160,180,200]

Ice_Cream_Sale = [20,40,60,80,100,120,140,160,180,200]

Drowning = {"Drowning_Accident": 
            [20,40,60,80,100,120,140,160,180,200],
            "Ice_Cream_Sale" :
            [20,40,60,80,100,120,140,160,180,200]}
Drowning = pd.DataFrame(data=Drowning)

Drowning.plot(x = "Ice_Cream_Sale", y="Drowning_Accident", kind = "scatter")
plt.show(block=True)

correlation_beach = Drowning.corr()
print(correlation_beach)

#Two lines to make our compiler able to draw:
plt.savefig(sys.stdout.buffer)
sys.stdout.flush()