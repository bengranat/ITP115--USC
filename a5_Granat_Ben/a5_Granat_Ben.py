# Benjamin Granat, bgranat@usc.edu
# ITP 115, Fall 2022
# Goomba
# Assignment 5
# User inputs a sentence and it counts total sum of special characters
# Also, it outputs number of occurences for each letter (capital and uncapitalized)

#Prompts user input
user_input = str(input("Enter a sentence: "))
count = 0

#Counts and prints number of special characters
for ch in user_input:
    if(ch != ' ' and not ch.isalpha()):
        count += 1
print('Special Characters: ', '*' * count)

#Appends list of empty array with all alphabets
#Also made count array with matching dictionary keys to keep track of counts
#For loops below for counting alphabet
alphabet = []
count2 = []
for i in range(65,91):
    alphabet.append(chr(i))
    count2.append(0)
for i in range(98,123):
    alphabet.append(chr(i))
    count2.append(0)
for i in range(0,56):
    for ch in user_input:
        if(ch == alphabet[i]):
            count2[i] += 1
        else:
            count2[i] == 0
#Final print statement for alphabet counts
    print(alphabet[i], ':', '*' * count2[i])

