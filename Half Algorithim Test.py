#!/usr/bin/env python
# coding: utf-8

# In[3]:


#!/usr/bin/env python
# coding: utf-8

# In[63]:

#Check button will have multiple choices, radio will have one- which one do we want?
#Leaning towards radio bc one graph spot right now

from tkinter import *
import tkinter as tk
from tkinter import ttk 
import os
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from scipy import stats
import random



root = Tk()
root.title('Resident Schedule Interface')
figure = Figure(figsize=(8, 6), dpi=100)
plot = figure.add_subplot(1, 1, 1)


rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU":4 , "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4, "Nuro": 4, "Clinic": 33, "OB2": 2 }
electives = ["InSrv1", "Card1", "Surg", "Emed", "ICU", "OB1", "PedC", "InSrv2", "NICU", "Nuro", "Clinic", "OB2"]
sessions = [4, 4, 14, 23, 4, 8, 4, 4, 4, 4, 33, 2]
z = list(zip(electives, sessions))
    #print("The original schedule for resident 1, year 1 is:" + str(rotations1))

    #step 2 on chart
def randomShuffle():
        random.shuffle(z)
        electives[:], sessions[:] = zip(*z)
        #print("the shuffled rotations are ")
       # print(electives, sessions)
    


def half():
        firstHalf = sessions[:len(sessions)//2]
        secondHalf = sessions[len(sessions)//2:]
        quarterRange = max(firstHalf) - max(secondHalf)
       # print(quarterRange)
        firstTotal = sum(firstHalf)
        secondTotal = sum(secondHalf)
        maxFirst = max(firstHalf)
        minFirst = min(firstHalf)
        maxSecond = max(secondHalf)
        minSecond = min(secondHalf)
        if quarterRange > maxSecond:
                maxFirst, maxSecond = minSecond, minFirst
                #print("Check works")
                half()
        else:
                #print("passed check")
                results = firstHalf + secondHalf
                #finalResults = dict(results)
                print("the new schedule is:" + str (results))
                keys = electives
                values = sessions
                quarters = np.array(results)
                np.split(quarters,4)
                print(quarters)
            
def testRun():
    randomShuffle()
    half()
    
for _ in range(5):
    testRun()
   
    

#Plot code: https://ishantheperson.github.io/posts/tkinter-matplotlib/
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)


# In[ ]:




