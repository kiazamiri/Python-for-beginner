# This is the Rock-Paper-Scissors Game. The players can quit the game
# by pressing n.

while True:
    play = input("do you want to play? (y/n) ")
    if play == "y":
        a = input('Player one, please enter your choice: ')
        b = input('Player two, please enter your choice: ')
        if a == b:
            print("It's a tie.")
        elif a.lower() == "rock":
            if b.lower() == "scissors":
                print("Player 1 Wins!")
            elif b.lower() == "paper":
                print("Player two Wins!")
            else:
                print("Invalid input! You have not entered rock, paper or scissors, try again.")
        elif a.lower() == "scissors":
            if b.lower() == "paper":
                print("Player 1 Wins!")
            elif b.lower() == "rock":
                print("Player two Wins!")
            else:
                print("Invalid input! You have not entered rock, paper or scissors, try again.")
        elif a.lower() == "paper":
            if b.lower() == "rock":
                print("Player 1 Wins!")
            elif b.lower() == "scissors":
                print("Player two Wins!")
            else:
                print("Invalid input! You have not entered rock, paper or scissors, try again.")
        else:
            print("Invalid input! You have not entered rock, paper or scissors, try again.")
    else:
        break
