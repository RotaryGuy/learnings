from random import randint
import os

selection = ""
player_score = 0
computer_score = 0

while (selection != "quit"):
    os.system('cls')
    print("Rock, Paper, Scissors!")
    print("----------------------")
    print("")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit the Game")
    print("")
    print(f"Player: {player_score} points. Computer: {computer_score} points.")
    choice = input("Choose: ")

    computer_selection = ""

    match choice:
        case "1":
            selection = "rock"
        case "2":
            selection = "paper"
        case "3":
            selection = "scissors"        
        case "4":
            selection = "quit"

    print(f"You chose {selection}")

    computer_choice = randint(0, 2) + 1

    match computer_choice:
        case 1:
            computer_selection = "rock"
        case 2:
            computer_selection = "paper"
        case 3:
            computer_selection = "scissors"        

    print(f"The computer chose: {computer_selection}")

    if (selection == computer_selection):
        print ("Tie!!")
    elif (selection == "rock"):
        if (computer_selection == "paper"):
            print ("You lost! Ha Ha")
            computer_score = computer_score + 1
        else:
            print ("You win!")
            player_score = player_score + 1
    elif (selection == "paper"):
        if (computer_selection == "scissors"):
            print ("You lost! Ha Ha")
            computer_score = computer_score + 1
        else:
            print ("You win!")        
            player_score = player_score + 1
    elif (selection == "scissors"):
        if (computer_selection == "rock"):
            print ("You lost! Ha Ha")
            computer_score = computer_score + 1
        else:
            print ("You win!")                
            player_score = player_score + 1
    print ("")
    input("Press Enter to continue...")
