
import collections
Iterable = getattr(collections, 'Iterable', None)

# Checks if the state of the tic tac toe is winning or not.
# The board consists of these elements:
#   >   1 - First mover token
#   >   -1 - Second mover token
#   >   0 - Empty
# Returns:
#   >   1 if first mover wins.
#   >   -1 if second mover wins
#   >   0 if tie
#   >   None if intermediate state
win_positions = (
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
)


def checkWinning(state: Iterable):
    if all(state):
        return 0
    for pos in win_positions:
        if state[pos[0]] == state[pos[1]] == state[pos[2]] and state[pos[0]] != 0:
            return 1 if state[pos[0]] == 1 else -1
    return None


# Positive score favor the first mover. Second mover favor the second mover
state_scores = {}
state_first_mover_moves = {}
state_second_mover_moves = {}


def recurse(state: Iterable, turn: int, level: int):
    # Check winning case. The lower the level, the smaller the score
    is_win = checkWinning(state)
    if is_win is not None:
        state_scores[ tuple(state) ] = is_win / (9 ** level)
        return state_scores[ tuple(state) ]

    # No winning. Try to insert current turn - Backtracking.
    sum_of_scores = 0
    max_scores = [ None, [] ]          # [Score, index]
    min_scores = [ None, [] ]          # [Score, index]
    for i in range(9):
        if state[i]: continue                   # Occupied Grid

        # Backtracking (1) - Replace current grid with turn token
        prev = state[i]
        state[i] = turn

        # Memoization - Previously computed value
        if tuple(state) in state_scores:
            score = state_scores[ tuple(state) ]
        else:
            score = recurse(state, -turn, level+1 )
        # Backtracking (2) - Put back previous value once done
        state[i] = prev

        sum_of_scores += score
        if max_scores[0] is None or max_scores[0] < score:
            max_scores[0] = score
            max_scores[1].clear()
            max_scores[1].append(i)
        elif max_scores[0] == score:
            max_scores[1].append(i)

        if min_scores[0] is None or min_scores[0] > score:
            min_scores[0] = score
            min_scores[1].clear()
            min_scores[1].append(i)
        elif min_scores[0] == score:
            min_scores[1].append(i)

    state_scores[ tuple(state) ] = sum_of_scores

    state_second_mover_moves[ tuple(state) ] = min_scores[1]
    state_first_mover_moves[ tuple(state) ] = max_scores[1]
    return sum_of_scores


INIT_STATE = [0,0,0,0,0,0,0,0,0]

EG_PLAYER_WINNING_0 = (0,0,-1,0,1,-1,0,0,1)   # Supposed move - 0
EG_PLAYER_WINNING_1 = (0,0,0,-1,1,0,-1,1,0)   # Supposed move - 1
EG_PLAYER_WINNING_2 = (-1,1,0,-1,1,0,1,-1,0)  # Supposed move - 2
EG_PLAYER_WINNING_3 = (0,-1,1,0,1,1,0,-1,-1)  # Supposed move - 3
EG_PLAYER_WINNING_4 = (-1,0,1,0,0,0,1,0,-1)   # Supposed move - 4
EG_PLAYER_WINNING_5 = (1,-1,-1,1,1,0,-1,0,0)  # Supposed move - 5
EG_PLAYER_WINNING_6 = (0,-1,1,0,-1,-1,0,1,1)  # Supposed move - 6
EG_PLAYER_WINNING_7 = (0,1,-1,-1,1,0,0,0,0)   # Supposed move - 7
EG_PLAYER_WINNING_8 = (1,0,-1,0,1,-1,0,0,0)   # Supposed move - 8

EG_PLAYER_LOSING_0 = (0,-1,-1,1,1,0,0,1,0)   # Supposed move - 0
EG_PLAYER_LOSING_1 = (0,0,0,-1,1,0,-1,1,0)   # Supposed move - 1
EG_PLAYER_LOSING_2 = (-1,1,0,-1,1,0,1,-1,0)  # Supposed move - 2
EG_PLAYER_LOSING_3 = (0,-1,1,0,1,1,0,-1,-1)  # Supposed move - 3
EG_PLAYER_LOSING_4 = (-1,0,1,0,0,0,1,0,-1)   # Supposed move - 4
EG_PLAYER_LOSING_5 = (1,-1,-1,1,1,0,-1,0,0)  # Supposed move - 5
EG_PLAYER_LOSING_6 = (0,-1,1,0,-1,-1,0,1,1)  # Supposed move - 6
EG_PLAYER_LOSING_7 = (0,1,-1,-1,1,0,0,0,0)   # Supposed move - 7
EG_PLAYER_LOSING_8 = (1,0,-1,0,1,-1,0,0,0)   # Supposed move - 8

EG_ENEMY_DEFEND_0 = (0,1,1,0,-1,0,0,0,0)     # Defend 0

recurse( INIT_STATE, 1, 0 )
for i in range(9):
    eval(f"print( state_scores[EG_PLAYER_WINNING_{i}] )")
    eval(f"print( state_first_mover_moves[EG_PLAYER_WINNING_{i}] )")
print("=" * 50)
for i in range(9):
    eval(f"print( state_scores[EG_PLAYER_LOSING_{i}] )")
    eval(f"print( state_second_mover_moves[EG_PLAYER_LOSING_{i}] )")
# print( state_scores[EG_ENEMY_DEFEND_0] )
# print( state_second_mover_moves[EG_ENEMY_DEFEND_0] )
