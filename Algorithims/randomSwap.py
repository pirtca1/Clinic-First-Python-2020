import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from scipy import stats


def swapPositions(yvalues): 
    random.shuffle(yvalues)
    return yvalues
  
yvalues = [45,32,44,53,48,87,79,48,70,77,75,81] 
pos1, pos2  = 1, 2

xvalues = [0,1,2,3,4,5,6,7,8,9,10,11]

slope, intercept, r_value, p_value, std_err = stats.linregress(xvalues, yvalues)
print("slope: %f    intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value**2)
print(swapPositions(yvalues)) 


while r_value < .9 :
    swapPositions(yvalues)
    slope, intercept, r_value, p_value, std_err = stats.linregress(xvalues, yvalues)
    print(swapPositions(yvalues))
    print("R-squared: %f" % r_value**2)
print(swapPositions(yvalues))
print("Done")
    
plt.plot(xvalues,yvalues)
plt.yscale('linear')
plt.title('Year_1')
plt.grid(True)

