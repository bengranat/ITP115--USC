# Name, USC email
# ITP 115, Fall 2022
# Section: Goomba
# Assignment 9
# Description:
# Translator
# User enter language and English words
# Outputs translations


# Function to read file for all languages in the header line
def readFileForLanguages(file_name):
    languages_file = open(file_name, "r")
    first_line = languages_file.readline()
    language_list = first_line.split(",")
    languages_file.close()
    return language_list


# Function gets user input for language (does not include English)
# Returns language chose by user
def getLanguageFromUser(language_list):
    print("Translate English words to one of the following languages:")
    available_languages = language_list[1:14]
    print(available_languages)
    count = 0
    while count == 0:
        user_input = input("Enter a language:")
        user_input = user_input.strip()
        user_input = user_input.capitalize()
        if user_input in available_languages:
            count += 1
            print("You have entered", user_input)
        else:
            print(user_input, "is not a valid language")
    return user_input

# Function will read file for words corresponding to chosen language
# Returns word list associated with language chosen by user
def readFileForWords(file_name, language_list, language_str):
    languages_file = open(file_name, "r")
    first_line = languages_file.readline()
    word_list = []
    index = language_list.index(language_str)
    for line in languages_file:
        line = line.strip()
        line_read = line.split(",")
        word_list.append(line_read[index])
    languages_file.close()
    return word_list


# Function to create .txt file with translations
# Prompts user to enter words untill return/enter button is pressed
# Stores index of english word list (created in main)
# Uses index to find corresponding translation
# Translation printed in corresponding .txt file
def createFileWithTranslations(language_str, english_list, word_list):
    translation_file = open(language_str + ".txt", "a")
    print("Words translated from English to " + language_str)
    user_input = input("Enter a word to translate (return to quit): ")
    while user_input != "":
        user_input.strip()
        if user_input in english_list:
            index = english_list.index(user_input)
            word_translation = word_list[index]
            if word_translation == "-":
                print(user_input, "did not have a translation.")
            else:
                print(user_input + " is translated to " + word_translation)
                print(user_input + " -> " + word_translation, file = translation_file)
        if user_input not in english_list:
            print(user_input, "is not in the English list.")
        user_input = input("Enter a word to translate (return to quit): ")
    print("Translated words have been saved to " + language_str + ".txt")
    translation_file.close()


def main():
    file_name = "languages.csv"

    #Stores list of possible languages
    language_list = readFileForLanguages(file_n4ame)

    #Stores english list
    english_list = readFileForWords(file_name, language_list, "English")

    #Stores language choise
    user_input = getLanguageFromUser(language_list)

    #Stores word list corresponding to chosen language
    word_list = readFileForWords(file_name, language_list, user_input)

    #Creates .txt files
    createFileWithTranslations(user_input, english_list, word_list)


main()