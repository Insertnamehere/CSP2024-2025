import math
start = None
while(start != 'start'):
    start = str(input("Welcome to the Airplane Travel Calculator, type 'start' to begin:  "))

print("You have ten feet of PVC pipe.")
print("You must make TWO cuts in order to make it into a triangle.")
cut01 = float(input("At what length would you like your FIRST cut:  "))
cut02 = float(input("At what length would you like your SECOND cut:  "))

sideA = cut01
sideB = cut02 - sideA
sideC = 10 - (sideA + sideB)
s = 10
area = math.sqrt(s * (s - sideA) * (s - sideB) * (s - sideC))

print("With cuts at", cut01, "and", cut02, "The sides of your new triangle have the dimentions of:  ", sideA, ",", sideB, "and", sideC)
print("Using Heron's Formula, inputing the respective value will output the area of the triangle which is:  ", area, ".")
