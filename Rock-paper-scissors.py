# Rock, Paper, Scissors in Python
import random

user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors. Best two out of three.\n")
computer = random.choice(['r', 'p', 's'])

computer_wins = 0
user_wins = 0

while user_wins < 3 and computer_wins < 3:
    user = user.lower()
    print(f"Computer chose {computer}")
    
    if user == computer:
        print('It\'s a tie')
    elif user == 'r' and computer == 's':
        print('You won!')
        user_wins += 1
    elif user == 'p' and computer == 'r':
        print('You won!')
        user_wins += 1
    elif user == 's' and computer == 'p':
        print('You won!')
        user_wins += 1
    elif user not in ['r', 'p', 's']:
        print('Invalid choice')
    else:
        print('You lost!')
        computer_wins += 1

    if user_wins == 3:
        print('You won the game!')
        break
    if computer_wins == 3:
        print('You lost the game!')
        break
    user = input("What's your next choice? \n")
    computer = random.choice(['r', 'p', 's'])
