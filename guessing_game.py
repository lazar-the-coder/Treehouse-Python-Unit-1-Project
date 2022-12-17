"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------
"""

import random

previous_scores = []
high_score = [100]
#you can change the range here, thus adjusting the difficulty
min_number = 1
max_number = 16

def start_game():
    #The welcome is separate so it doesn't appear every time.
    print("***Welcome to the number guessing game***\n***We will chose a number***\n***Try and guess what it is***")
    play_game()

def play_game():
    #collects name for high score chart.
    player_name = input("Please enter your name  ")
    #gets a number in the range
    answer_number = random.randint(min_number, max_number)
    guess_count = 0
    print("The previous heigh score was {}".format(high_score[0]))
    #Makes sure the loop starts by setting the guess not equal to answer
    guess_number = (answer_number - 1)
    print("The machine is thinking of a number between {} and {}".format(min_number, max_number))
    #When the guess matches, the loop stops
    while guess_number != answer_number:
        try:
            guess_number = int(input("Choose an integer  "))
            if guess_number < min_number or guess_number > max_number:
                print("thats not within the range")
            elif guess_number > answer_number:
                print("It's lower")
            elif guess_number < answer_number:
                print("It's higher")
            guess_count += 1
        #if the guess isn't an integer.
        except ValueError:
            print("thats not a integer")
    victory(player_name, guess_count)

def victory(player_name, guess_count):
    print("Got it")
    #adds scores to score list
    previous_scores.append([player_name, guess_count])
    print("***Congratulations on guessing the right number***\n***It took you", guess_count, "guesses***")
    #sets the new high score
    if guess_count < high_score[0]:
        high_score[0] = guess_count
        print("!!!You beat the high score!!!")
    #prints previous scores.
    print("***Here are the previous scores***")
    for score in previous_scores:
        print(score[0], ":", score[1])
    while True:
        answer = input("Want to play again? (Y/N)")
        if answer.lower() == "y":
            play_game()
            break
        elif answer.lower() == "n":
            print("Alright, thanks for playing.")
            break
        else:
            print("I didn't understand your answer")

start_game()
