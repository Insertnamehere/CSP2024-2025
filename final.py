import matplotlib.pyplot as plt
import numpy as np
import math

dataEx = np.loadtxt("stats.txt")

x = dataEx[:,0]
y = dataEx[:,1]
zip(x, y)

x.sort()

plt.plot(x, y, '-', color='purple')
plt.show()
