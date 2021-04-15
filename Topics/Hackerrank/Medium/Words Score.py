

def is_vowel(letter):
    return letter in ['a', 'e', 'i', 'o', 'u', 'y']


# Original function to debug provided by Hackerrank
def score_words(words):
    score = 0
    for word in words:
        num_vowels = 0
        for letter in word:
            if is_vowel(letter):
                num_vowels += 1
        if num_vowels % 2 == 0:
            score += 2
        else:
            score += 1              # There is no ++score in python
    return score


# Super compressed function
def score_words_2(words):
    score = sum( 1 if x % 2 else 2 for x in [ sum(is_vowel(letter) for letter in word) for word in words ] )
    return score