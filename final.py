import matplotlib.pyplot as plt
import numpy as np
import math

selectVar = 0

while(selectVar == 0):
    print("Welcome to Data Graphing and Calculations.\nPlease Select:\n0: Menu\n1: .txt file select\n2: Graph Data\n3: ")
    selectVar = int(input())

while(selectVar == 1):
    file = input("Write the full name of your file:\n")
    if(".txt" not in file):
        print("Please use file type such as .txt and try again")
        file = None
        selectVar = 1
    else:
        data = np.loadtxt(file)
        print("Successfully loaded!")
    

#dataEx = np.loadtxt()

#x = dataEx[:,0]
#y = dataEx[:,1]
#zip(x, y)

#x.sort()

#plt.plot(x, y, '-', color='purple')
#plt.show()
