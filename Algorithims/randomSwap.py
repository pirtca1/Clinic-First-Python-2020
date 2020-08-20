import random
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
from scipy import stats


def swapPositions(values): 
    random.shuffle(values)
    return values
  
#yearNumber = input("Type year number")

valuesOne = [45,32,44,53,48,87,79,48,70,77,75,81] 
ValuesTwo = [99,107,110	,108,113,96,123,100,114,119,110,100]
valuesThree = [133,127,117,126,115,127,121,104,122,121,110,128]

xvalues = [0,1,2,3,4,5,6,7,8,9,10,11]

slope, intercept, r_value, p_value, std_err = stats.linregress(xvalues, valuesOne)
print("slope: %f    intercept: %f" % (slope, intercept))
print("R-squared: %f" % r_value**2)
print(swapPositions(valuesOne)) 


while r_value < .9 :
    swapPositions(valuesOne)
    slope, intercept, r_value, p_value, std_err = stats.linregress(xvalues, valuesOne)
    print(swapPositions(valuesOne))
    print("R-squared: %f" % r_value**2)
print(swapPositions(valuesOne))
print("Done")
    
plt.plot(xvalues,valuesOne)
plt.yscale('linear')
plt.title('Year_1')
plt.grid(True)
