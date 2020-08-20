import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from scipy import stats


def swapPositions(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    m, b = np.polyfit(listXvalues, listYvalues, 1)
    
    return list 
  
listYvalues = [45,32,44,53,48,87,79,48,70,77,75,81] 
pos1, pos2  = 1, 2

listXvalues = [0,1,2,3,4,5,6,7,8,9,10,11]

slope, intercept, r_value, p_value, std_err = stats.linregress(listXvalues, listYvalues)
print("slope: %f    intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value**2)
print(swapPositions(listYvalues, pos1-1, pos2-1)) 

while r_value < .8:
    swapPositions(listYvalues, pos1-1, pos2-1)

plt.plot(listXvalues,listYvalues)
plt.yscale('linear')
plt.title('Year_1')
plt.grid(True)



