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

"""
PLAYER_NAME = ""
PLAYER_PLAY = []
PLAYER_WINS = []
total_games = 5
import random

def welcome():
    # welcoming the player
    # May decide who will play first (can be implemented at a later stage)
    print("Welcome! Human, Welcome to the game of life and death")
    PLAYER_NAME = input("Share your name Human!: ")
    print("\n Let the Game Begin! \n \n")
    return PLAYER_NAME


def game_play(PLAYER_NAME):
    # defines the game play
    options = ['rock', 'paper', 'scissor']
    player_choice = input(f"Enter your choice {PLAYER_NAME}? Your options are {options} \n").lower()
    computer_choice = random.choice(options)
    return player_choice, computer_choice

def play_win(player_choice, computer_choice):
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
       return "Computer"
   if player_choice== "paper" and computer_choice=="scissor":
       return "Computer"
   return "Computer"

def main():
    PLAYER_NAME = welcome()
    for game in range(total_games):

        print(f"\n This is the game {game+1} ")
        print("*" * 25)
        player_choice, computer_choice = game_play(PLAYER_NAME)
        print(f"{PLAYER_NAME},  you have chosen {player_choice} and I have chose {computer_choice} \n")

        winner = play_win(player_choice, computer_choice)
        if winner == "Draw":
            print(f"You Lucky Shot. This time I will win \n")
            PLAYER_WINS.append("Draw")
        elif winner == "Computer":
            print(f"You may Cry. I win \n")
            PLAYER_WINS.append("Lost")
        else: # winner == PLAYER_NAME:
            print(f"Congratulations {PLAYER_NAME} you win the round {game+1} \n")
            PLAYER_WINS.append("Win")
        print("*" * 25)
        print(f"Game {game+1} ends")
        PLAYER_PLAY.append(f"game")

    print("\n The Utimate showdown in here")
    print("-" * 25)

    if PLAYER_WINS.count("Win") < PLAYER_WINS.count("Lost"):
        print("The mighty computer is the winner")
    elif PLAYER_WINS.count("Win") > PLAYER_WINS.count("Lost"):
        print(f"Hurray!!!! {PLAYER_NAME} wins!")
    else:
        print("What a Boring Draw")

if __name__ == "__main__":
    main()
