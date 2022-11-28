import random

print('-' * 60)
print('\t\t << [ Guess the Number ] >>')
print('-' * 60)
#Title Header

initial_balance_is_valid = False

while not initial_balance_is_valid:
    try:
        initial_balance = float(input('\nHow much money do you want to play ?: '))
        if initial_balance > 0:
            initial_balance_is_valid = True
        else:
            print("You can't bet 0 or negative amount of money !")
    except ValueError:
        print('Enter a numeric amount, like 100 or 40.50.')

print("\n\t       --- Excellent. Let's start. ---")
#Getting the user funds and bet

game_is_playing = True
gains = []
#Starting the game
while game_is_playing:

    bet_is_valid = False

    while bet_is_valid is not True:
        try:
            bet = float(input('\nEnter your bet amount:  '))
            if bet <= initial_balance + sum(gains) and bet > 0:
                bet_is_valid = True
            else:
                print("You can't bet 0, negative amount of money or money that you don't have !")
        except ValueError:
            print('Please enter a valid number.')
#Getting the valid number to guess
    guess_number_is_valid = False

    while not guess_number_is_valid :
        try:
            guess_number = float(input('Guess number?:   '))
            if 0 <= guess_number <= 36:
                guess_number_is_valid = True                
            else:
                print("You have to enter a number between 0 and 36 !")
        except ValueError:
            print('Please enter a valid number.')
#If the guess is not a valid number, redo getting the number
   
    # initializing list

    winning_number = [ 0, 1, 2, 3, 4, 5, 6 ,7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    
    random_num = random.choice(winning_number)
#Randomizing the possible result
    
    if guess_number == random_num:        
        gain = bet * 3
    else:
        gain = -bet
#effects by the bet on the funds
    if gain > 0:
        print("Winning number is : " + str(random_num))
        print('You won', gain)
        gains.append(gain)
#When the user wins
    else:
        print("Winning number is : " + str(random_num))
        print('You loss', -gain)
        gains.append(gain)
#When the user lose
    balance_final = initial_balance + sum(gains)
    print('Your balance is now', balance_final)
#Showing the final balance
    if balance_final == 0:
        print('-' * 60)
        print('Sorry. You are bankrupt.')
        break
#When the funds is 0 balance or unable to bet
    replay_is_valid = False

    while not replay_is_valid :
        replay = input('Do you want to play again ? Type yes or no 🙂')
        if replay == 'no':
            game_is_playing = False
#Asking user to play again
            print('-' * 60)
            print('Initial balance:', initial_balance)
            if gain <=0:
                print('Loss: ', -sum(gains))
            else:
                print('Gain: ', sum(gains))
#Gain or Loss



            print('Balance:', balance_final)
#Showing funds
            print('-' * 60)
            print('See you next time.')
            break
        elif replay == 'yes' or replay == 'no':
            replay_is_valid = True
        elif replay == 'yes':
            game_is_playing = True

        else:
            print('Just enter yes or no.')
#End/Terminating Program