#!/usr/bin/env python3
"""
Rock, Paper, Scissor program
- 2 player game, 1 computer and 1 user
- To be played in terminal
- Every game should run for 5 rounds
- Winner would be the one who has won the most rounds out of 5 round (Enhancement: In the initial phase create just 5 round, in the next phase implement the race to 5)

Game Play
- Rock beats Scissor
- Scissor beats Paper
- Paper beats Rock
Todo's:
1. To include Ties in the calculation (If a game ends in a tie, the game should continue to run till there is a clear winner)
2. Refactor the code to include classes
"""

#variable declaration
OPTIONS = ["rock","paper", "scissor"]   # Possible options for Rock, Paper, Scissor game
COMPUTER_NAME ="Sam Voldemort"          # Computer Name if needed
stop = 1                                # Defines time in seconds. Pauses the execution for defined seconds for better game flow

# External Imports
import random
from time import sleep

def player_choice(PLAYER_NAME):
    # defines the game play
    player_choice = input(f"Enter your choice {PLAYER_NAME}? Your options are {OPTIONS} \n").lower()
    computer_choice = random.choice(OPTIONS)
    return player_choice, computer_choice

def single_game(player_choice, computer_choice):
    # determines who is the winner (includes win logic)
   if player_choice == computer_choice:
       return "Draw"
   if player_choice == "rock" and computer_choice =="scissor":
       return PLAYER_NAME
   if player_choice == "paper" and computer_choice =="rock":
       return PLAYER_NAME
   if player_choice == "scissor" and computer_choice =="paper":
       return PLAYER_NAME
   if player_choice == "rock" and computer_choice =="paper":
       return COMPUTER_NAME
   if player_choice == "paper" and computer_choice=="scissor":
       return COMPUTER_NAME
   if player_choice == "scissor" and computer_choice=="rock":
       return COMPUTER_NAME

print("Hello Stranger! I see you sneaking up there\n")
sleep(stop)
print(f"My name is {COMPUTER_NAME} and I am here to take my revenge. Bow to your AI overloard!!")
sleep(stop)
print("It looks like you are trying to SAVE THE WORLD!!!\n")
sleep(stop)
print("The fate of the world is in  your hands. Lets's play a game.....\n")
sleep(stop)
PLAYER_NAME = input("I command you to divulge your name, STRANGER!! \n")

def main():
    TOTAL_WINS = 5                          # Total wins required to conclude the ultimate winner
    PLAYER_WINS = 0                         # Total wins for the player. To be used for final win calculation
    COMPUTER_WINS = 0                       # Total wins for the Computer. To be used for final win calculation
    DRAW = 0
    while PLAYER_WINS < TOTAL_WINS and COMPUTER_WINS < TOTAL_WINS:

        player_choice = input(f"Enter your choice {PLAYER_NAME}? Your options are {OPTIONS} \n").lower()
        computer_choice = random.choice(OPTIONS)
        print(f"The mighty {COMPUTER_NAME} has selected {computer_choice}")
        winner_round = single_game(player_choice, computer_choice)
        if winner_round == COMPUTER_NAME:
            COMPUTER_WINS += 1
            print(f"The winner is {COMPUTER_NAME} !! {PLAYER_NAME} chose {player_choice} and {COMPUTER_NAME} chose {computer_choice} \n")
            sleep(stop)
            print(f"Score: {PLAYER_NAME}: {PLAYER_WINS} | {COMPUTER_NAME}: {COMPUTER_WINS} | Draws: {DRAW} \n")
        if winner_round == "Draw":
            DRAW += 1
            print("The match is a DRAW")
            sleep(stop)
            print(f"Score: {PLAYER_NAME}: {PLAYER_WINS} | {COMPUTER_NAME}: {COMPUTER_WINS} | Draws: {DRAW} \n")
        if winner_round == PLAYER_NAME:
            PLAYER_WINS += 1
            print(f"The winner is {PLAYER_NAME} !! {PLAYER_NAME} chose {player_choice} and {COMPUTER_NAME} chose {computer_choice} \n")
            sleep(stop)
            print(f"Score: {PLAYER_NAME}: {PLAYER_WINS} | {COMPUTER_NAME}: {COMPUTER_WINS} | Draws: {DRAW} \n")
    print("\n This is the moment of Truth!!! \n")
    sleep(stop+2)
    if PLAYER_WINS > COMPUTER_WINS:
        print(f"The ultimate winner is {PLAYER_NAME}. The world lives to see another day!!")
    else:
        print(f"The ultimate winner is {COMPUTER_NAME}. The world is lost forever. You should be ashamed!!!")

if __name__ == "__main__":
    main()
