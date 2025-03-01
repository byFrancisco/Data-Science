#define la liner regresion usando python 
#What is Calorie_Burnage if Average_Pulse is: 120, 130, 150, 180?

def Predict_Calorie_Burnage(Average_Pulse):
 return(0.3296 * Average_Pulse + 346.8662)
 
#Try some different values:
print(Predict_Calorie_Burnage(120))
print(Predict_Calorie_Burnage(130))
print(Predict_Calorie_Burnage(150))
print(Predict_Calorie_Burnage(180))