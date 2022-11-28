import random

print('-' * 60)
print('\t\t << [ MINI COINFLIP ] >>')
print('-' * 60)
#Title Header
while True:
    user_bet = input("Enter a choice (head, tail): ")
    user_choice = ["head", "tail"]
    computer_action = random.choice(user_choice)
    print(f"\nYou bet on {user_bet}, The winning coin is {computer_action}.\n")
#Getting user input, Randomizing the answer
    if user_bet == computer_action:
        print("Congrats, Your fund is now 2x! ")
#If the user win
    elif user_bet != computer_action:
        print("Nice Try, Better luck next time! ")
#If the user loss
    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
#Asking the to play again and Terminating the program