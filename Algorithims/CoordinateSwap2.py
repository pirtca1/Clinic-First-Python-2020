%matplotlib inline
import matplotlib.pyplot as plt
plt.style.use('seaborn=whitegrid')
import numpy as np



def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    m, b = np.polyfit(listXvalues, listYvalues, 1)
    return list 
  
listXvalues = [23,67,34,76,42,12,55,45,71,45,55,31] 
pos1, pos2  = 1, 2
  
listYvalues = [0,1,2,3,4,5,6,7,8,9,10,11]


print(swapPositions(listXvalues, pos1-1, pos2-1)) 


