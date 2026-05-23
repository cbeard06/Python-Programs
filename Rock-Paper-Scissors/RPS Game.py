# Rock Paper Scissors

import random

choices = ["Rock", "Paper", "Scissors"]

running = True

def showscore():
    print(f"\nScore:\nYou - {playerWins}\nComputer - {computerWins}\n-------------------------")

print('Welcome to Rock Paper Scissors! \nThis game is first to 3 wins \nRock beats Scissors, Scissors beats Paper, and Paper beats Rock!'
'\nEnter "Q" at any time to quit the game!\n--Connor Beard\n-------------------------')

while running:
    
    computerWins = 0
    playerWins = 0
    
    while (playerWins < 3) and (computerWins <3):
    
        computerChoice = random.choice(choices)
        playerChoice = input("\nRock, Paper, or Scissors? \n\n")

        if playerChoice == "Q" or playerChoice == "q":
            running = False
            break
    
        if playerChoice == computerChoice:
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("Tie!")
            showscore()
        elif playerChoice == "Rock" and computerChoice == "Scissors":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("You win this round!")
            playerWins += 1
            showscore()
        elif playerChoice == "Scissors" and computerChoice == "Rock":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("Computer wins this round!")
            computerWins += 1
            showscore()
        elif playerChoice == "Paper" and computerChoice == "Scissors":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("Computer wins this round!")
            computerWins += 1
            showscore()
        elif playerChoice == "Scissors" and computerChoice == "Paper":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("You win this round!")
            playerWins += 1
            showscore()
        elif playerChoice == "Paper" and computerChoice == "Rock":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("You win this round!")
            playerWins += 1
            showscore()
        elif playerChoice == "Rock" and computerChoice == "Paper":
            print(f"\nPlayer chose: {playerChoice}")
            print(f"Computer chose: {computerChoice}")
            print("Computer wins this round!")
            computerWins += 1
            showscore()
        else:
            print("\nInvalid option!")

    if not running:
        break
    
    
    if playerWins == 3:
        print(f"\nScore: \nYou - {playerWins} \nComputer - {computerWins} \nYou win!\n-------------------------")
    elif computerWins == 3:
        print(f"\nScore: \nYou - {playerWins} \nComputer - {computerWins} \nComputer wins!\n-------------------------")
    else:
        print("\nSee you next time!\n-------------------------")
    again = input("\nRematch? (Y/N): \n").upper()
    if again != "Y" or again == "Q":
        print("Thanks for playing!")
        input("\nPress Enter to quit...")
        break
    else:
        print("-------------------------")
