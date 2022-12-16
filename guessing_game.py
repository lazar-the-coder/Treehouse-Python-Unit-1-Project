"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

high_scores = []

def start_game():
    print("***Welcome to the number guessing game***\n***We will chose a number***\n***Try and guess what it is***")
    play_game()

def play_game():
    player_name = input("Please enter your name  ")
    answer_number = random.randint(0, 15)
    guess_count = 1
    guess_number = input("Choose a number from 0 to 15  ")
    while guess_number != str(answer_number):
        try:
            guess_number = int(guess_number)
            if guess_number < 0:
                print("thats not between 0 and 15")
            elif guess_number > 15:
                print("thats not between 0 and 15")
            elif guess_number > answer_number:
                print("It's lower")
            elif guess_number < answer_number:
                print("It's higher")
            guess_count += 1
        except ValueError:
            print("thats not a number")
        
        guess_number = input("Choose again  ")
    victory(player_name, guess_count)

def victory(player_name, guess_count):
    print("Got it")
    high_scores.append([player_name, guess_count])
    print("***Congratulations on guessing the right number***\n***It took you", guess_count, "guesses***")
    print("***Here are the high scores***")
    for score in high_scores:
        print(score[0], ":", score[1])
    while True:
        answer = input("Want to play again? (Y/N)")
        if answer.lower() == "y":
            play_game()
        elif answer.lower() == "n":
            print("Alright, thanks for playing.")
            exit()
        else:
            print("I didn't understand your answer")

start_game()
