#Betting Game 
import csv
import sys
def main():
   menu()


def menu():
    
    print("\n")
    print("\t      ------[ Welcome to CAZINO ]----- ")
    print()

    choice = input("""
                   1: Rock-Paper-Scissors
                   2: GuessTheNumber
                   3: MiniCoinFlip
                   

               Please enter your choice: """)

    if choice == "1":
        print ("\n")
        import rps
    elif choice == "2":
        print ("\n")
        import gn 
    elif choice == "3":
        print ("\n")
        import cf
    else:
        choice == "0"
        sys.exit
   
    menu()


    
#the program is initiated,

main()