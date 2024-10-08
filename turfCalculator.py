start = 'false'
while(start != 'start'):
    start = str(input("Welcome to the Turf Calculator, type 'start' to begin:  "))
print("*Please answer with numbers only. Will not work if not*")
turfL = float(input("Please enter the Length of the field in feet:  "))
turfW = float(input("Please enter the Width of the field in feet:  "))
turfCost = float(input("Please enter the price of the field per square foot:  "))

perimeter = (turfL * 2) + (turfW * 2)
area = turfL * turfW
totalPrice = turfCost * area
print("Here's the dimetions and cost of your new turf field:")
print("The perimeter of the field would be: ", perimeter, "feet.")
print("The area of the field is: ", area, "square feet.")
print("With the price set at", turfCost, "the total would be: ", totalPrice, "Dolars.")