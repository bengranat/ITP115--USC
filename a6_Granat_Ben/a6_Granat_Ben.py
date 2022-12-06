# Benjamin Granat, bgranat@usc.edu
# ITP 115, Fall 2022
# Goomba
# Assignment 6
# The user will try to guess a word based on that word's jumbled letters.
# There will be three words to choose from with a hint for each.
# You only get one hint.

#Setting all necessary variables for the game
import random as rand
#List of words and hints
words = ["volkswagen", "python", "undeniable"]
hints = ["think cars", "think programming", "Michael Jordan is the ___ GOAT"]
#Empty strings and ints necessary for later use
word_list = []
jumbl_word = ''
jumbl_letters = ''
user_guess = ''
user_hint = ''
guess_count = 0
#Initializes play_again variable
play_again = input(print("Welcome to the jumbling game! Would you like to play?"))

#While loop for game
while play_again != "N" and play_again != "n":
    guess_count = 0
    index = rand.randint(0, 2)
    word_list = list(words[index])
#For loop to iterate through each random letter and add to new word
    for i in range(0, len(words[index])):
        jumbl_letters = rand.choice(word_list)
        jumbl_word += jumbl_letters
        word_list.remove(jumbl_letters)
#User guesses the word
    user_guess = input(print("Enter your guess: ", jumbl_word))
#If statements to check user input against true word
    if user_guess != words[index]:
        guess_count += 1
        user_hint = print(input("Incorrect guess! Would you like a hint? Type Y or N:"))
        if user_hint == "Y" or play_again != "y":
            print(hints[index])
            user_guess = input(print("Enter your guess: ", jumbl_word))
        else:
            user_guess = input(print("Enter your guess: ", jumbl_word))
#If statement to prompt end of game
    if user_guess == words[index]:
        print("Well done! You have correctly guessed the word!")
        print("It took you", guess_count, "tries.")
        word_list = []
        jumbl_word = ''
        jumbl_letters = ''
        user_guess = ''
        user_hint = ''
    play_again = input(print("Would you like to play again? Type Y or N: "))