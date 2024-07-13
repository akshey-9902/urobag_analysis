import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from main import *
from object import *
from color import *
from main2 import *


# Data points (x, y)
x = np.array([2.67890625, 4.122137405, 6.190794979, 7.008088235, 9.529411765, 9.44516129, 
              10.01647059, 12.21328125, 11.68363636, 16.3575, 15.21098901, 14.81086957, 
              18.68535565, 18.26266094, 18.54961832, 19.66329114, 21.39230769, 21.38161765, 
              22.32145749, 22.65132743])
y = np.array([100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1600, 1700, 1800, 1900, 2000])

# Function to model and create data
def poly_fit(x, a, b, c):
    return a * x**2 + b * x + c

# Curve fitting


# Plotting the data and the fitted curve
# plt.figure(figsize=(10, 5))
# plt.scatter(x, y, label='Data points')
# plt.plot(np.sort(x), poly_fit(np.sort(x), *popt), label='Fitted Curve', color='red')
# plt.title('Curve Fitting')
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.show()
def final(link):
    popt, pcov = curve_fit(poly_fit, x, y)
    m=pixel2(link)
    print(m[1]-m[0]+1)
    f=factor(link)
    print(f)
    print((m[1]-m[0]+1)*f)
    vol=(poly_fit((m[1]-m[0]+1)*f, *popt))
    #print(vol)
    col=color('im1.jpeg')
    #print(col)
    dict = {'r': col[0], 'g': col[1], 'b': col[2], 'vol': vol,}
    

    json_output = json.dumps(dict)
    return(json_output)

#final()
    
    