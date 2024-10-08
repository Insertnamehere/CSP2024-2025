start = 'false'
while(start != 'start'):
    start = str(input("Welcome to the Airplane Travel Calculator, type 'start' to begin:  "))

travDest = str(input("Welcome, please input your travel destination:  "))
travDist = float(input("How far is the distance in miles:  "))
planeSpeed = float(input("What is the average speed the air plane is going in Miles Per Hour:  "))
windAve = float(input("What is the average wind speed in miles per hour. Please use positive numbers for wind going with the plane and negitive numbers for going against the plane:  "))

realSpeed = planeSpeed + windAve
print(realSpeed)

totalTime = round(travDist / realSpeed, 2)
print("The time it will take to travel", travDist, "to", travDest, "going", planeSpeed, "with", windAve, "average wind speed will be:  ", totalTime, "hours.")

