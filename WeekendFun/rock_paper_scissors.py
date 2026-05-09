#-Get choices and standardise them
#-Compare the three choice with if, elif statements and print results

player_one = input("Player 1 (rock, paper, scissors): ").lower().strip()
player_two = input("Player 2 (rock, paper, scissors): ").lower().strip()

if player_one == player_two:
    print("Tie")
else:
    if player_one == "rock":
        if player_two == "scissors":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    elif player_one == "paper":
        if player_two == "rock":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
            
    elif player_one == "scissors":
        if player_two == "paper":
            print("Player 1 wins")
        else:
            print("Player 2 wins")
    else:
        print("Invalid input!")
