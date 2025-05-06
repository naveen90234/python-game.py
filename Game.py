import random

l = ["rock", "scissor", "paper"]

while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start...
1. Yes
2. No
Enter your choice: '''))

    if uc == 1:
        for a in range(1, 6):
            userinput = int(input('''
1. Rock
2. Scissor
3. Paper
Enter your choice: '''))

            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "scissor"
            elif userinput == 3:
                uchoice = "paper"
            else:
                print("Invalid input")
                continue

            Cchoice = random.choice(l)

            if Cchoice == uchoice:
                print("Computer chose:", Cchoice)
                print("You chose:", uchoice)
                print("Game Draw")
                ucount += 1
                ccount += 1
            elif (uchoice == "rock" and Cchoice == "scissor") or (uchoice == "paper" and Cchoice == "rock") or (uchoice == "scissor" and Cchoice == "paper"):
                print("Computer chose:", Cchoice)
                print("You chose:", uchoice)
                print("You Win!")
                ucount += 1
            else:
                print("Computer chose:", Cchoice)
                print("You chose:", uchoice)
                print("Computer Wins!")
                ccount += 1

        print("\nFinal Score:")
        print("Your Score:", ucount)
        print("Computer Score:", ccount)

        if ucount > ccount:
            print("Congratulations! You won the game.")
        elif ccount > ucount:
            print("Computer wins the game. Better luck next time!")
        else:
            print("The game is a Draw!")

    else:
        break
