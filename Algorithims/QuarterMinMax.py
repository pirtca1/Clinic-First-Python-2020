#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 13:39:55 2020

@author: pirtca1
"""
import matplotlib.pyplot as plt
import random
import numpy as np
#step 1 on chart
rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4 , "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4, "Nuro": 4, "Clinic": 33, "OB2": 2 }

print("The original schedule for resident 1, year 1 is:" + str(rotations1))

#step 2 on chart
def rotationShuffle():
    global r1
    r1 = list(rotations1.items())
    random.shuffle(r1)
    return r1

rotationShuffle()
newRotations1 = dict(r1)

#third step 
def quarterGet(lst, n):
    global fourSplit
    sessions = list(newRotations1.values())
    fourSplit = np.array_split(sessions, 4)
    return fourSplit, sessions
class Quarter:

    def quarterCreate():
        global qAll
        q1 = [fourSplit[0]]
        q2 = [fourSplit[1]]
        q3 = [fourSplit[2]]
        q4 = [fourSplit[3]]
        qAll = [q1, q2, q3, q4]
        return q1, q2,q3, q4, qAll
    def quarterMaxMin(qAll):
        for max in qAll:
                qMax = max
        for min in qAll:
                qMin = min
        quarterRange = qMax - qMin
        return quarterRange
    def quarterSwap(q1, q2, q3, q4, quarterRange):
            if sum(q1) or sum(q2) or sum(q3) or sum(q4) >= quarterRange:
                 for min in zip(q1, q2, q3, q4):
                     min(random.choice(q1,q2,q3,q4)) == max(random.choice(q1, q2, q3, q4))
            else:
                    print(r1)
                    rotationShuffle()
                    quarterGet(sessions, 3)
            
    def ____call____(self):
        self.quarterCreate()
        self.quarterMaxMin()
        self.quarterSwap()
sessions = list(newRotations1.values())
quarterGet(sessions, 3)
quarter = Quarter
quarter()
quarter.quarterCreate()
quarter.quarterMaxMin([qAll])
quarter.quarterSwap()


#final step
print("the new schedules are:" + str (r1))
keys = newRotations1.keys()
values = newRotations1.values()
plt.bar(keys, values)
