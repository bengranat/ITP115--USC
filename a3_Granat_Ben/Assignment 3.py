# Ben Granat, bgranat@usc.edu
# ITP 115, Fall 2022
# Goomba
# Assignment 3
# Program creates a vending machine where
# user enters payment and program determine change

# Options for vending machine:
print("Welcome! Here are the following options:")
print("a) Assortment of candy for 11 Sickles and 7 Knuts")
print("b) Butterbeer for 2 Sickles")
print("c) Quail for 6 Sickles")
print("d) Daily Prophet for 5 Knuts")

# Input variables:
inp = str(input("Choose one: "))
sickles_inp = int(input("How many Sickles do you have?: "))
knuts_inp = int(input("How many Knuts do you have?: "))
galleons_inp = int(input("How many galleons do you have?: "))

# Costs for each choice and total input value
a_cost = 326
b_cost = 58
c_cost = 174
d_cost = 2465
total_inp = (sickles_inp)*29 + knuts_inp + (galleons_inp)*493

# Calculates change in Knuts for each purchase and converts back into sickles, galleons, knuts
galleons_change_a = (total_inp - a_cost)//493
sickles_change_a = (total_inp - galleons_change_a*493)//29
knuts_change_a = total_inp - sickles_change_a*29 - galleons_change_a*493

galleons_change_b = (total_inp - b_cost)//493
sickles_change_b = (total_inp - galleons_change_b*493)//29
knuts_change_b = total_inp - sickles_change_b*29 - galleons_change_b*493

galleons_change_c = (total_inp - c_cost)//493
sickles_change_c = (total_inp - galleons_change_c*493)//29
knuts_change_c = total_inp - sickles_change_c*29 - galleons_change_c*493

galleons_change_d = (total_inp - d_cost)//493
sickles_change_d = (total_inp - galleons_change_d*493)//29
knuts_change_d = total_inp - sickles_change_d*29 - galleons_change_d*493

# Output for vending machine through series of if statements
if inp == "a" or inp == "A":
    if total_inp >= a_cost:
        print("You purchased the Assortment of candy.")
        print("Change = ", galleons_change_a, "galleons, ", sickles_change_a, "sickles, and ",
            knuts_change_a, "knuts")
    else:
        print("You do not have enough knuts to go through with purchase.")
elif inp == "b" or inp == "B":
    if total_inp >= b_cost:
        print("You purchased the Butterbeer.")
        print("Change = ", galleons_change_b, "galleons, ", sickles_change_b, "sickles, and ",
            knuts_change_b, "knuts")
    else:
        print("You do not have enough knuts to go through with purchase.")
elif inp == "c" or inp == "C":
    if total_inp >= c_cost:
        print("You purchased the Quail.")
        print("Change = ", galleons_change_c, "galleons, ", sickles_change_c, "sickles, and ",
            knuts_change_c, "knuts")
    else:
        print("You do not have enough knuts to go through with purchase.")
elif inp == "d" or inp == "D":
    if total_inp >= d_cost:
        print("You purchased the Daily Prophet.")
        print("Change = ", galleons_change_d, "galleons, ", sickles_change_d, "sickles, and ",
            knuts_change_d, "knuts")
    else:
        print("You do not have enough knuts to go through with purchase.")
else:
    print("You entered an invalid choice.")