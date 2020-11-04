from tkinter import *
import tkinter as tk
from tkinter import ttk 
import os
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



        
def randomSwapCall():
    valuesOne = [4, 4, 14, 23, 4, 8, 4, 4, 4, 4, 33, 2] 
    xvalues = ["InSrv1", "Card1", "Surg", "Emed", "ICU", "OB1", "PedC", "InSrv2", "NICU", "Nuro", "Clinic", "OB2"]
    z = list(zip(xvalues, valuesOne))
    random.shuffle(z)
    valuesOne[:],xvalues[:] = zip(*z)
    plot.plot(valuesOne,xvalues)
    canvas.draw()
    print(z) 
    
    
def continuityCall():
    import numpy as np

# step 1 on chart
    rotations1 = {"InSrv1": 4, "Card1": 4, "Surg": 14, "Emed": 23, "ICU": 4, "OB1": 8, "PedC": 4, "InSrv2": 4, "NICU": 4,
              "Nuro": 4, "Clinic": 33, "OB2": 2}

    #print("The original schedule for resident 1, year 1 is:" + str(rotations1))

# step 2 on chart
    r1 = list(rotations1.items())
    random.shuffle(r1)

    #print(r1)

    newRotations1 = dict(rotations1)
    #print("the new schedule is:" + str(r1))


    def rotationShuffle():
        newRotations1 = dict(rotations1)
        #print("the new schedule is:" + str(newRotations1))  # otherwise str (r1)


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
        #Can use as metric to see if it is worth keeping, if current quarter range better than best
            # fourth and fifth step

        def sumCalc(self, q):
            sum = 0
            for k in q:
                val = int(k[1])
                sum = sum + val
            return sum


    rotationShuffle()
    #sessions1 = list(newRotations1.values())

    sessions1 = r1


    fourSplit = quarterGet(sessions1, 4)

    #print('The foursplit value is :')


    quarter = Quarter()
    #quarter()
    (q1,q2,q3,q4) = quarter.quarterCreate(fourSplit)
    #print(quarter.sumCalc(q1), q1)
    #print(q2)
    #print(q3)
    #print(q4)

    (qMax, qMin, quarterRange) = quarter.quarterMaxMin(q1,q2,q3,q4)



    # final step
    print("the new schedules are:" + str(r1))
    




def levelCall():
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
                randomShuffle()
                half()
        else:
                #print("passed check")
                results = firstHalf + secondHalf
                #finalResults = dict(results)
                print("the new schedule is:" + str (results))
                keys = electives
                values = sessions
                #plt.bar(keys, values)
                #Replicate the random graph (Total number of sessions)
           
    randomShuffle()
    half()
    plot.plot(electives, sessions)
    canvas.draw()

    
#Makes the popup 
def makeMenu():
    def checkCombo():
        plot.clear()
        if selection.get() == 'Continuity':
            plot.clear()
            plot.set_title("1 Resident Schedule: Continuity")
            plot.set_xlabel("Rotation")
            plot.set_ylabel("Number of Clinic Sessions a Month")
            continuityCall()
            window.destroy()
            
            
        if selection.get() == 'Random':
            plot.clear()
            plot.set_title("1 Resident Schedule: Random")
            plot.set_xlabel("Month")
            plot.set_ylabel("Number of Clinic Sessions a Month")
            randomSwapCall()
            window.destroy()
      
            
        if selection.get() == 'Level Loading':
            plot.clear()
            plot.set_title("1 Resident Schedule: Level Loading")
            plot.set_xlabel("Rotation")
            plot.set_ylabel("Number of Clinic Sessions a Month")
            levelCall()
            window.destroy()
            
        else:
            checkCombo()
            plot.clear()
    window = tk.Tk() 
    window.title('Choose Algorithim') 
    window.geometry('550x250') 
    btn = tk.Button(window, text = "Select", command = checkCombo)
    btn.grid(column = 3, row = 5, padx = 5, pady = 15)
    n = tk.StringVar() 
    combo = ttk.Combobox(content, width = 27, textvariable = n )
    ttk.Label(window, text = "Select an Algorithim:", 
          ).grid(column = 0, 
          row = 5, padx = 10, pady = 25) 
    
    selection = ttk.Combobox(window, width = 27, textvariable = n) 
    selection['values'] = ('Continuity', 'Level Loading', 'Random')
    selection.grid(column = 1, row = 5)
    selection.current()
     
content = tk.Frame(root)
frame = tk.Frame(content, borderwidth = 5, width = 800, height = 650)

def exportFile():
    fig = plot.get_figure()
    fig.savefig('schedule.png')
    print("Saved!")
    
upload = tk.Button(content, text = "Upload Data")
generate = tk.Button(content, text = "Choose Algorithim", command = makeMenu)
exportChoice = tk.Button(content, text = "Export", command = exportFile)

content.grid(column = 0, row =0)
frame.grid(column = 0, row = 0, columnspan = 3, rowspan = 2)

upload.grid(column = 0, row = 4, columnspan = 1, sticky=( S, E, W))
generate.grid(column = 1, row = 4, columnspan = 1, sticky=( S, E, W))
exportChoice.grid(column = 2, row = 4, columnspan = 1, sticky=( S, E, W))

root.columnconfigure(0, weight=10)
root.rowconfigure(0, weight=10)
content.columnconfigure(0, weight=30, pad= 3)
content.columnconfigure(1, weight=30, pad= 3)
content.columnconfigure(2, weight=30, pad= 3)
content.columnconfigure(3, weight=10, pad= 3)
content.columnconfigure(4, weight=10, pad= 3)
content.rowconfigure(1, weight=10)

#Plot code: https://ishantheperson.github.io/posts/tkinter-matplotlib/
canvas = FigureCanvasTkAgg(figure, root)
canvas.get_tk_widget().grid(row=0, column=0)

root.mainloop()
