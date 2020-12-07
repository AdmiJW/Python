from collections import Counter


# This problem, from first glance, can be misleading at first, leading us to think of complicated and advanced
# string matching algorithms if the problem is not read properly

# What we really need to do is, for every valid substring that can be formed, the score either goes to Stuart
# or Kevin depending on the first alphabet is vowel or not.
# So, in linear time O(N) by iterating through every possible starting characters in the string, we can obtain the
# number of substrings that can be formed by formula
#           length - idx
# and that's it!


# Two pass method using sum()
def minion_game(string: str) -> None:
    length = len(string)
    vowel_score = sum(length - i for i, c in enumerate(string) if is_vowel(c))
    cons_score = sum(length - i for i, c in enumerate(string) if not is_vowel(c))

    print(f'Kevin {vowel_score}' if vowel_score > cons_score else f'Stuart {cons_score}' if cons_score > vowel_score
    else 'Draw')


# One pass solution
def minion_game(string: str) -> None:
    kevin, stuart = 0, 0
    length = len(string)

    for i, c in enumerate(string):
        if is_vowel(c):
            kevin += length - i
        else:
            stuart += length - i

    print(f'Kevin {kevin}' if kevin > stuart else f'Stuart {stuart}' if stuart > kevin
    else 'Draw')


# Notice that from 1 to N, number of combinations: 1 + 2 + 3 ... N, so use formula (n)(n+1) / 2 instead
def minion_game2(string: str) -> None:
    length = len(string)
    vowel_score = sum(length - i for i, c in enumerate(string) if is_vowel(c))
    cons_score = (length * (length + 1)) // 2 - vowel_score

    print(f'Kevin {vowel_score}' if vowel_score > cons_score else f'Stuart {cons_score}' if cons_score > vowel_score
    else 'Draw')


def is_vowel(string: str) -> bool:
    return string in 'AEIOU'


if __name__ == '__main__':
    cnt = Counter([])
