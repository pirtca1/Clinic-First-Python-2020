import matplotlib.pyplot as plt
import random
import numpy as np
#step 1 on chart
rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4 , "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4, "Nuro": 4, "Clinic": 33, "OB2": 2 }
electives = ["InSrv1", "Card1", "Surg", "Emed", "ICU", "OB1", "PedC", "InSrv2", "NICU", "Nuro", "Clinic", "OB2"]
sessions = [4, 4, 14, 23, 4, 8, 4, 4, 4, 4, 33, 2]
z = list(zip(electives, sessions))
#print("The original schedule for resident 1, year 1 is:" + str(rotations1))

#step 2 on chart
def randomShuffle():
    random.shuffle(z)
    electives[:], sessions[:] = zip(*z)
    print("the shuffled rotations are ")
    print(electives, sessions)
    


def half():
    firstHalf = sessions[:len(sessions)//2]
    secondHalf = sessions[len(sessions)//2:]
    quarterRange = max(firstHalf) - max(secondHalf)
    print(quarterRange)
    firstTotal = sum(firstHalf)
    secondTotal = sum(secondHalf)
    maxFirst = max(firstHalf)
    minFirst = min(firstHalf)
    maxSecond = max(secondHalf)
    minSecond = min(secondHalf)
    if quarterRange > -29:
            maxFirst, maxSecond = minSecond, minFirst
            print("Check works")
            randomShuffle()
            half()
    else:
            print("passed check")
            results = firstHalf + secondHalf
            #finalResults = dict(results)
            print("the new schedule is:" + str (results))
            keys = electives
            values = sessions
            plt.bar(keys, values)
           
randomShuffle()
half()

