import pandas as pd
import statsmodels.formula.api as smf

full_health_data = pd.read_csv("Math/DSAVANCED/datos.csv",header=0, sep=",")

model = smf.ols('Hours_Work ~ Hours_Sleep', data = full_health_data)
results = model.fit()
print(results.summary())