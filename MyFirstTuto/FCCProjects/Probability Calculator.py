import copy
import random
from typing import List, Dict
from collections import Counter


class Hat:
    #   Since the contents need to be mutated, but recovered each time draw() is called, we kept a copylist to recover
    #   to initialization state
    def __init__(self, **balls:(str,int) ) -> None:
        self.contents = [ k for k in balls for i in range(balls[k] ) ]
        self.copylist = copy.copy(self.contents)

    #   Every time draw() is called, contents need to be recovered into initialization state, so we copy back
    def draw(self, num: int) -> List:
        self.contents = copy.copy(self.copylist)
        #   Since we are drawing without replacement, we use pop()
        result = [ self.contents.pop(random.randint(0, len(self.contents) - 1) )
                 for i in range(num) if len(self.contents) > 0]
        return result


def experiment(hat: Hat, expected_balls: Dict, num_balls_drawn: int, num_experiments: int) -> float:
    count = 0

    for i in range(num_experiments):
        #   Uses a counter object to help count the frequencies in the draw list returned
        #   Another good thing is that it will not return KeyError, but instead only 0
        attempt = Counter( hat.draw(num_balls_drawn) )

        #   If the loop is terminated by break, then it won't run the else clause.
        for keys in expected_balls:
            if attempt[keys] < expected_balls[keys]:
                break
        else:
            count += 1

    return count / num_experiments


