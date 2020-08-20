import numpy as np
import matplotlib.pyplot as plt
import random
from random import shuffle

rotations1 = {"Inpt_Serv": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4 , "OB1": 8, "PedC": 4, "Inpt_Serv": 4, "NICU": 4, "Neuro": 4, "Clinic": 33, "OB2": 2 }

print("The original schedule for resident 1, year 1 is:" + str(rotations1))

r1 = list(rotations1.items())
random.shuffle(r1)
rotations1 = dict(r1)

print("the new schedule is:" + str (rotations1))
keys = rotations1.keys()
values = rotations1.values()
plt.bar(keys, values)
