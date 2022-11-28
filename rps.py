import random

print('-' * 60)
print('\t\t << [ Rock-Paper-Scissors ] >>')
print('-' * 60)
#Title Header
while True:
    user_bet = input("Enter a choice (rock, paper, scissors): ")
    user_choice = ["rock", "paper", "scissors"]
    computer_action = random.choice(user_choice)
    print(f"\nYou chose {user_bet}, computer chose {computer_action}.\n")
    #Declaring Variables, Setting up Conditions, Getting Users Input

    if user_bet  == computer_action:
        print(f"Both players selected {user_bet}. It's a tie!")
        #Logic when both user and computer has the same answer
    elif user_bet == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
        #Logic when user win by using rock
        else:
            print("Paper covers rock! You lose.")
        #Logic when user lose using rock
    elif user_bet == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
        #Logic when user win by using paper
        else:
            print("Scissors cuts paper! You lose.")
        #Logic when user lose by using paper
    elif user_bet == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
        #Logic when user win by using scissors
        else:
            print("Rock smashes scissors! You lose.")
        #Logic when user win by using paper

    play_again = input("Play again? (yes/no): ")
    if play_again.lower() != "yes":
        break
    #When deciding to play again