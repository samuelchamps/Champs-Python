#from getpass import getpass as input
print("ROCK, PAPER AND SCISSOR")
print("Type R - Rock, S - Scissors, P - Paper")
player_1 = input("Player 1 > ").lower()
print(player_1)

player_2 = input("Player 2 > ").lower()
print(player_2)

if player_1 == "r" and player_2 == "s":
    print(f"Player 1 Won!")
elif player_1 == "r" and player_2 == "r":
    print(f"Draw")
elif player_1 == "r" and player_2 == "p":
    print(f"Player 2 Won!")
elif player_1 == "s" and player_2 == "r":
    print(f"Player 2 Won!")
elif player_1 == "s" and player_2 == "s":
    print(f"Draw")
elif player_1 == "s" and player_2 == "p":
    print(f"Player 1 Won!")
elif player_1 == "p" and player_2 == "r":
    print(f"Player 1 Won!")
elif player_1 == "p" and player_2 == "p":
    print(f"Draw")
elif player_1 == "p" and player_2 == "s":
    print(f"Player 2 Won!")
