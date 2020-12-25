from collections import Counter


# ---------------------------------------------------------------------------------------------------
# Pass in the status of two teams, scoreA and scoreB
# Will return a Tuple of size 3 which
#       first value is boolean where True indicate a winner is determined, False means game continues
#       second value is tuple which shows the score of both teams (A,B)
#       third value shows the winning team, 'A' or 'B' if any, or None if not settled yet
# ---------------------------------------------------------------------------------------------------
def score_checker(statusA, statusB):
    scoreA, scoreB = sum(statusA), sum(statusB)
    score_tuple = (scoreA, scoreB)

    # Equal score means the game is not settled
    if scoreA == scoreB:
        return False, (scoreA, scoreB), None

    # Both team played complete 10 games. We need to check which team is the winner
    # Notice that if the game ends in tie, the above if statement will already taken care
    if len(statusA) == 5 and len(statusB) == 5:
        return True, (scoreA, scoreB), 'A' if scoreA > scoreB else 'B'

    attempt_left_A = 5 - len(statusA)
    attempt_left_B = 5 - len(statusB)

    # If it is no longer possible for a team to catch up with the other team marks, immediately return True (other team
    # already win although haven't progressed full 10 games) and stop further Depth First Search for this one
    if scoreA + attempt_left_A < scoreB:
        return True, score_tuple, 'B'
    elif scoreB + attempt_left_B < scoreA:
        return True, score_tuple, 'A'

    # Otherwise, full 10 games haven't completed yet and other team may catch up anytime soon. Continue
    return False, score_tuple, None

# ------------------------------------------------------------------------------------------
# The backtracking function
# ------------------------------------------------------------------------------------------
def backtracker(statusA, statusB):
    check, score_tuple, winner = score_checker(statusA, statusB)

    # It is set here to retrieve winner of team A only. Remove winner == 'A' to retrieve all winning positions
    if check and winner == 'A':
        res.add( ( tuple(statusA), tuple(statusB), score_tuple, winner) )
        return
    # Base case. No more further backtracking
    if len(statusA) >= 5 and len(statusB) >= 5:
        return

    # Its Team A's turn
    if len(statusA) == len(statusB):
        statusA.append(1)
        backtracker(statusA, statusB)
        statusA.pop()

        statusA.append(0)
        backtracker(statusA, statusB)
        statusA.pop()

    # Otherwise it is Team B's turn
    else:
        statusB.append(1)
        backtracker(statusA, statusB)
        statusB.pop()

        statusB.append(0)
        backtracker(statusA, statusB)
        statusB.pop()




def comparator(elem):
    return len(elem[0]), len(elem[1]), elem[2]


# Global variable set for storing result
# Each entry should contain format of
#       (Status of TeamA), (Status of TeamB), (Scores), (Winning Team)
res = set()
backtracker([], [])
res = sorted( res, key=comparator )
[ print(x) for x in res ]

# Prints the total number of ways Team A win
print( len(res) )

# Prints Frequecy of all winning case's score breakdown
# ( scoreA, scoreB ): Frequency
freq = Counter( x[2] for x in res )
print( freq)

# Prints frequency of all winning case's - number of kicks
# required for winning
freqlen = Counter( len(x[0]) + len(x[1]) for x in res )
print(freqlen)
