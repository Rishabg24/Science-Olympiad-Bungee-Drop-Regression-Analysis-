'''
Use commented code if you are running trials to check how well your function is doing. 
This will save simulation runs where the cord length makes sense as an excel sheet called SimMod.
Cord lengths that are not feasible will be put into an excel spreadsheet called Incorrect_lengths.  
''' 

import random
import pandas as pd

def Calculate(x,y):
  # x in grams. y in cm
  z = 0.00144*x**2 + -0.00124*x*y + -0.00008*y**2 + -0.45887*x + 0.92831*y + 4.99952 # Example Function
  return z

count = 0
Incorrect_lengths = []
Simulation_runs = []


number_runs = 100 # Change this as needed
for i in range(0,number_runs):

  g = random.randint(50, 300)
  d = random.randint(200, 500)
  z = Calculate(g,d)


  # if(z<d):
  #   SimMod.append({"Mass": g, "Drop_Height": d, "Cord_Length": z})
  #   count+=1
  # else:
  #   incorrect.append({"Mass": g, "Drop_Height": d, "Cord_Length": z})
  #   continue

  print("Mass: " + str(g))
  print("Drop Height: " + str(d))
  print("Cord Lenght: " + str(z) + '\n')

# Finding how many times function is correct

print("=======================================")
print("Number of Runs: " + str(count))
print("=======================================")
print("Accuracy: " + str((count/number_runs)*100))
print("=======================================")

# print("Number of incorrect lengths: " + str(len(incorrect_lengths)))
# bf = pd.DataFrame(Incorrect_lengths)
# df = pd.DataFrame(SimMod)
# df.to_excel("Simulation_runs.xlsx", index = False)
# bf.to_excel("Incorrect_lengths.xlsx", index = False)
