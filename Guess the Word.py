"""
Filename: Guess the Word.py
Author: Jesslyn Zhen
Date: 30 / 06 / 22
Description: This is a program that will randomly select a word from a list. The user then has as many tries as they need to guess the word, but they are only allowed a maximum of 6 incorrect answers.
There are 2 different game modes for the user to choose from. 
"""

# Import random to choose randomly from lists later
import random

# Initialise Constants, Variables & Lists
WORDS = ["JAZZ","ABRUPTLY","FOUND","SUNSHINE","PYTHON","SPRING","FALL","AUTUMN","WINTER","SUMMER","MOUNTAINS","AWKWARD","REQUIRE","UNIQUE"]
SCRAMBLED_WORDS = ["AZJZ","UYLRBAPT","UDFNO","NHSNUEIS"]
ALPHABET = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
VALID_CHOICE = ["1","2","3"]
MAX_INCORRECT = 6
random_word = random.choice(WORDS)
current_word = "*" * len(random_word)
incorrect_guess = 0
guessed_letters = []
user_choice = "0"
user_continue = True

while user_continue:
    user_choice = "0"
    print("""\n\nHello & Welcome! This is a Guess the Word program. You can guess as many times as you want, however, you are only allowed a maximum of 6 incorrect answers. There are 2 game modes you can play:
1. Hangman
2. Sort the Letters
3. Exit Program

What would you like to do?\n""")
 
    # Ask for user's choice (1-3) & validate their input
    user_choice = input("Please enter a number (1-3): ").strip()
    while not user_choice in VALID_CHOICE:
        user_choice = input("You did not enter a number (1-3). Please try again: ").strip()

    # Massive IF statement (+ nested IF statements) for each menu choice
    if user_choice == "1": # Start Hangman Game
        while incorrect_guess < MAX_INCORRECT and current_word != random_word:
            print("\nThe word is:", current_word)
            print("\nSo far, you have guessed the following letters:\n", guessed_letters)
            print("\nNumber of incorrect guesses so far:", incorrect_guess)

            user_guess = input("\nPlease enter a letter: ").strip()
            user_guess = user_guess.upper()
            
            while user_guess in guessed_letters:
                print("You have already guessed the letter ", user_guess)
                user_guess = input("\nPlease enter another letter: ").strip()
                user_guess = user_guess.upper()
            guessed_letters.append(user_guess)

            if user_guess in random_word:
                print("Good job! The letter", user_guess, "is in the word!")

                # New variable to include user's guess
                new_word = ""
                
                for i in range(len(random_word)):
                    if user_guess == random_word[i]:
                        new_word += user_guess
                    else:
                        new_word += current_word[i]
                current_word = new_word

            else:
                print("\nSorry, the letter", user_guess, "isn't in the word.")
                incorrect_guess += 1

        if incorrect_guess == MAX_INCORRECT:
            print("\nUnfortunately, you did not manage to guess the word.")
        else:
            print("\nCongratulations! You guessed the word!")

        print("\nThe word was:", random_word)
            
    elif user_choice == "2": # Start Sort the Letters Game
        print("Sort the Letters game will be done in the next iteration!")
    else: # Exit Program as we know the user's input is definitely 3 (input has already been validated earlier)
        print("Thanks for playing! See you soon :D")
        user_continue = False


