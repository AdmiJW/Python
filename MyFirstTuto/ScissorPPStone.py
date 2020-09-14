"""
Rock paper scissor stone game testing
"""

import random as rand

if __name__ == "__main__":
    switcher = {
        0: "Scissor",
        1: "Paper",
        2: "Stone"
    }
    moves = {
        'sci': 0, 'scissor': 0,
        'sto': 2, 'stone': 2,
        'pp': 1, 'paper': 1
    }
    while True:
        cpuMove = rand.randint(0, 2)

        playerMove = input("Make your move: ").lower()
        while playerMove not in moves:
            playerMove = input("Invalid move! (Hint: sci, pp, sto or full name works): ").lower()
        playerMove = moves.get(playerMove)

        print('You do %s while CPU does %s' % (switcher.get(playerMove), switcher.get(cpuMove)))

        # If the cpu move and player move is of the same
        if cpuMove == playerMove:
            print("Draw. Starting a new round...")

        # If the cpu plays Scissor
        elif cpuMove == 0:
            if playerMove == 1: print("You lose")
            else: print("You win")

        # If the cpu plays Paper
        elif cpuMove == 1:
            if playerMove == 0: print("You win")
            else: print("You lose")

        # If the cpu plays Rock
        else:
            if playerMove == 0: print("You lose")
            else: print("You win")

        print("-" * 50)
