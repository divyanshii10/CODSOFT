#INSTRUCTIONS:
#  1. You are playing against the computer.
#  2. Rock beats scissor, scissor beat paper, and paper beats rock.
#  3. You can play again by entering yes or no.

import random

def play_game():
  
  while(True):
    print("\n---Welcome to the Rock, Paper, Scissor Game!!----\n")
    print("---You're playing against the computer.---\n")
    
    choices = ['rock','paper','scissor']
    #ask user to enter their choice.
    user_choice = input("Enter your choice (rock, paper, or scissor): ").lower()

    if user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissor only.")
        return

    computer_choice = random.choice(choices)

    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("It's a tie!")
    elif(
        (user_choice == 'rock' and computer_choice == 'scissor') or
        (user_choice == 'paper' and computer_choice == 'rock') or
        (user_choice == 'scissor' and computer_choice == 'paper')
    ):
        print("You win!")
    else:
        print("Computer wins!")
    
    #ask user to play again
    play_again = input("Do you want to play again?(yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        break

play_game()
