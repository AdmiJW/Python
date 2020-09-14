import random


def random_walk(steps: int) -> int:
    location = [0, 0]
    for i in range(steps):
        direction = random.choice([(1, 0), (-1, 0), (0, 1), (0, -1)])
        location[0] += direction[0]
        location[1] += direction[1]
    return abs(location[0]) + abs(location[1])


for steps in range(1, 60):
    over5 = sum(random_walk(steps) <= 4 for i in range(20000))
    print('%d Steps: %f%% occurrences within 5 block' %(steps, over5 / 200) )
