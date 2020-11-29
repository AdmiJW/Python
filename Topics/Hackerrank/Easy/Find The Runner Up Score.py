
import functools as ft

if __name__ == '__main__':
    N = int(input() )
    scores = tuple(int(x) for x in input().split() )

    # Two pass method: Find max, then find 2nd max which is below max
    max_score = max(scores)
    second = ft.reduce(lambda acc, val: val if acc < val < max_score else acc, scores, -float('inf') )
    print(second)


    # Sorting method. O(n log n) time complexity, descending order
    scores = sorted(scores, reverse=True)
    for sc in scores:
        if sc != scores[0]:
            print(sc)
            break

    # Set sorting to avoid sorting duplicates
    score_set = set( scores )
    print( sorted(score_set, reverse=True)[1] )
