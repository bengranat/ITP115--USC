# Ben Granat, bgranat@usc.edu
# ITP 115, Fall 2022
# Goomba
# Lab 3a
answer = str
while answer != "q" and answer != "Q":
    answer = input("Choose one of: a) Favorite Animal, f) Favorite Food, p) Favorite Place, q) Quit ")
    if answer == "a" or answer == "A":
        print("a > My favorite animal is the lion.")
    elif answer == "f" or answer == "F":
        print("f > My favorite food is chicken and rice.")
    elif answer == "p" or answer == "P":
        print("p > My favorite place is Croatia.")
    else:
        print("That option is not available.")