import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from operator import itemgetter
import matplotlib.colors as mcolors
import os
import time
import math

import settings as st

selectVar = 0
dataFile = None
n = 0

while(True):
    while(selectVar == 0):
        print("Welcome to Data Graphing and Calculations.\nPlease Select:\n0: Menu\n1: .txt file select\n2: Register Data\n3: Graph Data\n4: Settings\n5: Exit")
        selectVar = int(input())
        
    while(selectVar == 4):
        settingVar = input("0: Menu\n1: Visual Custumization\n2: Graphing")
        '''while(settingVar == 1):
            visCustumVar = input("0: Settings\n1: Main Graph Color\n2: Line Style\n")
            while(visCustumVar == 1):
                st.graphColorMain = input("Please select color.")
                if(st.graphColorMain not in mcolors.CSS4_COLORS):
                    print("Not a valid color. Try again.")
                else:
                    print("Done")
                    time.sleep(.75)
                    visCustumVar = 0'''
        while(settingVar == 2):
            graphingVar = input("0: Settings\n1: Sort by -",st.sortBy,"\n2: Sort Reversed -", st.sortReverse)
            while(graphingVar == 1):
                st.sortBy = input("x or y\n")
            while(graphingVar == 2):
                st.sortReverse = input("True or False\n")
                    
    while(selectVar == 1):
        file = input("Write the full name of your file:\n")
        if(".txt" not in file):
            print("Please use file type such as .txt and try again")
            file = None
            selectVar = 1
        else:
            if(os.path.exists(file) == False):
                print("File not found. Please try again.")
            else:
                dataRaw = np.loadtxt(file)
                print("Successfully loaded!")
                time.sleep(.75)
                selectVar = 0
    
    while(selectVar == 2 and file != None):

        x = dataRaw[:,0]
        y = dataRaw[:,1]
        
        dataTplOg = list(zip(x,y))
        tplSort = sorted(dataTplOg, key= itemgetter(n))
        
        print(tplSort)

        xSort, ySort = zip(*tplSort)
        
        plt.plot(xSort, ySort, '-', color=settings.graphColorMain)
        plt.show()
