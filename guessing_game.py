"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces. 

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

high_scores = []
min_number = 1
max_number = 16

def start_game():
    print("***Welcome to the number guessing game***\n***We will chose a number***\n***Try and guess what it is***")
    play_game()

def play_game():
    player_name = input("Please enter your name  ")
    answer_number = random.randint(min_number, max_number)
    guess_count = 0
    guess_number = (answer_number - 1)
    print("The machine is thinking of a number between {} and {}".format(min_number, max_number))
    while guess_number != answer_number:
        try:
            guess_number = int(input("Choose a number  "))
            if guess_number < min_number or guess_number > max_number:
                print("thats not within the range")
            elif guess_number > answer_number:
                print("It's lower")
            elif guess_number < answer_number:
                print("It's higher")
            guess_count += 1
        except ValueError:
            print("thats not a number")
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
