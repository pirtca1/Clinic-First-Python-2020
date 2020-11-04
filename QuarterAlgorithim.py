#Having a seed to "choose" what to base the random value on good for future work
# step1
import random
import numpy as np

# step 1 on chart
rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU": 4, "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4,
              "Nuro": 4, "Clinic": 33, "OB2": 2}

print("The original schedule for resident 1, year 1 is:" + str(rotations1))

# step 2 on chart
r1 = list(rotations1.items())
random.shuffle(r1)

print(r1)

newRotations1 = dict(rotations1)
print("the new schedule is:" + str(r1))


def rotationShuffle():
    newRotations1 = dict(rotations1)
    print("the new schedule is:" + str(newRotations1))  # otherwise str (r1)


# third step
def quarterGet(lst, n):
    sessions = list(newRotations1.values())
    fourSplit = np.array_split(lst, n)
    return fourSplit
    return sessions


class Quarter:
    def quarterCreate(self, fourSplit):
        q1 = fourSplit[0]
        q2 = fourSplit[1]
        q3 = fourSplit[2]
        q4 = fourSplit[3]
        qAll = [q1, q2, q3, q4]
        #return q1, q2, q3, q4, qAll
        return qAll

    def quarterMaxMin(self, q1, q2, q3, q4):
        qMax = 0
        qMin = 100
        for q in (q1,q2,q3,q4):
            for k in q:
                val = int(k[1])
                if qMax < val:
                    qMax = val
                if qMin > val:
                    qMin = val

       # print(f'qMax = {qMax}')
        #print(f'qMin = {qMin}')
        quarterRange = qMax - qMin
       # print(f'quarterRange = {quarterRange}')
        return (qMax,qMin,quarterRange)
        # fourth and fifth step

    def sumCalc(self, q):
        sum = 0
        for k in q:
            val = int(k[1])
            sum = sum + val
        return sum
    

   
      

""" def quarterSwap(self, q1, q2, q3, q4, quarterRange):
        if self.sumCalc(q1) >= quarterRange or self.sumCalc(q2) >= quarterRange or self.sumCalc(q3) >= quarterRange or self.sumCalc(q4) >= quarterRange:
            #needs fixing from here, what are we trying to do? 
         pass
"""



rotationShuffle()
#sessions1 = list(newRotations1.values())

sessions1 = r1


fourSplit = quarterGet(sessions1, 4)

print('The foursplit value is :')


quarter = Quarter()
#quarter()
(q1,q2,q3,q4) = quarter.quarterCreate(fourSplit)
#print(quarter.sumCalc(q1), q1)
#print(q2)
#print(q3)
print(q4)

(qMax, qMin, quarterRange) = quarter.quarterMaxMin(q1,q2,q3,q4)



# final step
print("the new schedules are:" + str(r1))

