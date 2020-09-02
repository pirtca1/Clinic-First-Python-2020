import matplotlib.pyplot as plt
import random

rotations1 = {"InSrv": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4 , "OB1": 8, "PedC": 4, "InSrv": 4, "NICU": 4, "Nuro": 4, "Clinic": 33, "OB2": 2 }

print("The original schedule for resident 1, year 1 is:" + str(rotations1))


def rotationShuffle():
    global r1
    r1 = list(rotations1.items())
    random.shuffle(r1)
    return r1

rotationShuffle()
newRotations1 = dict(r1)
print("the new schedule is:" + str (r1))
keys = newRotations1.keys()
values = newRotations1.values()
plt.bar(keys, values)
