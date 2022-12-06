# Ben Granat, bgranat@usc.edu
# ITP 115, Fall 2022
# Goomba
# Assignment 4
# User inputs array of numbers
# Program calculates the avg, min, and max of the array

#Setting variables for list, avg, min, and max
x = []
avg = 0
minimum = 0
maximum = 0
inp = int(input("Input an integer greater than or equal to 0 or -1 to quit:"))

#While loop which appneds list and finds avg, min, max
while inp != -1:
    x.append(inp)
    avg = sum(x)/len(x)
    minimum = min(x)
    maximum = max(x)
    inp = int(input("Input an integer greater than or equal to 0 or -1 to quit:"))

#Series of print statements
print("The average of your set is:", avg)
print("The minimum of your set is:", minimum)
print("The maximum of your set is:", maximum)