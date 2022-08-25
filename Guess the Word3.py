"""
Filename: Guess the Word3.py
Author: Jesslyn Zhen
Date: 30 / 06 / 22
Description: This is a program that will randomly select a word from a list. The user has to guess the word with a maximum of 6 incorrect answers. There are 2 different game modes for the user to choose from.
"""

# Import random to choose randomly from lists, & import time to use timer in STL
import random
import time

# Initialise Constants, Variables & Lists
WORDS = ["JAZZ", "ABRUPTLY", "FOUND", "SUNSHINE", "SHADOW", "SPRING", "FALL", "AUTUMN", "WINTER", "SUMMER", "MOUNTAINS", "AWKWARD", "REQUIRE", "UNIQUE"]
SCRAMBLED_WORDS = ["AZJZ", "UYLRBAPT", "UDFNO", "NHSNUEIS", "WDHASO", "RGSIPN", "ALFL", "UUMATN", "RIWTNE", "MUSRME", "ITUMNASON", "DWKRAWA", "EQRIRUE", "NQEIUU"]
VALID_CHOICE = ["1", "2", "3"]
MAX_INCORRECT = 6
user_continue = True

while user_continue:
    # Variables below must be reset after each game
    random_word = random.choice(WORDS)
    random_scrambled = random.choice(SCRAMBLED_WORDS)
    current_word = "*" * len(random_word)
    incorrect_guess = 0
    guessed_letters = []
    guessed_words = []
    random_scrambled = random.choice(SCRAMBLED_WORDS)
    user_word = ""

    print("""\n\nHello & Welcome! This is a Guess the Word program. The game ends once you have guessed the word or made 6 incorrect guesses. There are 2 game modes you can play:
1. Hangman
2. Sort the Letters (60 seconds to unscramble the word)
3. Exit Program

What would you like to do?\n""")

    # Ask for user's choice (1-3) & validate their input
    user_choice = input("Please enter a number (1-3): ").strip()
    while user_choice not in VALID_CHOICE:
        user_choice = input("You did not enter a number (1-3). Please try again: ").strip()

    # Massive IF statement (+ nested IF statements) for each menu choice
    if user_choice == "1":  # Start Hangman Game
        while incorrect_guess < MAX_INCORRECT and current_word != random_word:
            print("\nThe word is: {}".format(current_word))
            print("\nGuessed letters so far: ")
            print(" ".join(guessed_letters))
            print("\nNumber of incorrect guesses so far: {}".format(incorrect_guess))

            # Flag to check for valid input, set to False at the start
            valid_input = False
            while not valid_input:
                user_guess = input("\nPlease enter a letter: ").strip()
                user_guess = user_guess.upper()
                if user_guess.isalpha() is False or len(user_guess) > 1:
                    print("\nYou did not enter a letter. Please try again.")
                elif user_guess in guessed_letters:
                    print("\nYou have already guessed this letter!")
                elif user_guess not in guessed_letters:
                    guessed_letters.append(user_guess)
                    # If the user enters correct input, set flag to True
                    valid_input = True

            if user_guess in random_word:
                print("\nGood job! The letter {} is in the word!".format(user_guess))

                # New variable to include user's guess
                new_word = ""
                for x in range(len(random_word)):
                    if user_guess == random_word[x]:
                        new_word += user_guess
                    else:
                        new_word += current_word[x]
                current_word = new_word
            else:
                print("\nSorry, the letter {} isn't in the word.".format(user_guess))
                incorrect_guess += 1

        if incorrect_guess == MAX_INCORRECT:
            print("\nUnfortunately, you did not manage to guess the word.")
        else:
            print("\nCongratulations! You guessed the word!")

        print("\nThe word was: {}".format(random_word))

    elif user_choice == "2":  # Start Sort the Letters Game
        for i in range(len(SCRAMBLED_WORDS)):
            if random_scrambled == SCRAMBLED_WORDS[i]:
                actual_word = WORDS[i]
        print("\nYou have 60 seconds to guess the word, good luck!")
        time_remaining = 60
        start_time = time.time()
        while incorrect_guess < MAX_INCORRECT and user_word != actual_word and time_remaining > 0:
            print("\nThe word is: {}".format(random_scrambled))
            print("\nNumber of incorrect guesses so far: {}".format(incorrect_guess))

            user_word = input("\nPlease guess a word: ").strip()
            while not user_word.isalpha() or len(user_word) < 1:
                user_word = input("You did not enter a word. Please try again: ").strip()
            user_word = user_word.upper()

            new_time = time.time()
            time_remaining = 60 + start_time - new_time

            if time_remaining <= 0:
                print("\nUnfortunately, time is up, you did not manage to guess the word.")
                continue
            else:
                print("\nTime remaining is ", "{:.0f}".format(time_remaining), " seconds")

            if user_word == actual_word:
                print("\nCongratulations! You guessed the word!")
            else:
                print("\nSorry, that isn't the word.")
                incorrect_guess += 1

            if incorrect_guess == MAX_INCORRECT:
                print("\nUnfortunately, you did not manage to guess the word.")

        print("\nThe scrambled word was: {}".format(actual_word))

    else:  # Exit Program as we know the user's input is definitely 3 (input has already been validated earlier)
        print("Thanks for playing! See you soon :D")
        user_continue = False
