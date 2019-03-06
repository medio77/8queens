from scipy.stats import boltzmann
import matplotlib.pyplot as plt
import numpy as np
import math
list=[]
temp=50
for i in range(0,50):
    list.append(math.exp(-1 * abs((10)) / temp))
    temp=temp-1

plt.plot(list)

plt.show()
