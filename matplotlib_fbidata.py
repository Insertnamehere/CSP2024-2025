import matplotlib.pyplot as plt
#import matplotlib.artist as mart
#import pandas as pd
import numpy as np

#crimeData = pd.read_csv("FBI_DATA.txt", sep='\s+', header = 0)
crimeData = np.loadtxt('FBI_DATA.txt')

x = crimeData[:,0]
y = crimeData[:,1]

#lineClr = str(input("Pick a line color: red, blue, green, purple  "))
#markerType = str(input("Pick a marker type: X, *, o, v  "))


#fig, ax = plt.subplots()
#plt.ion()
plt.plot(x, y, '-', color='purple')
plt.ylabel('Violent Crime')
plt.xlabel('Year')
plt.show()
