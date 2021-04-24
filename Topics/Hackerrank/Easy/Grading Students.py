
# Rule: 1. If below 38, no rounding
#       2. If N % 5 >= 3, round up by adding (5 - N%5)


def gradingStudents(grades):
    return map(lambda x: x if x < 38 or x % 5 < 3 else x + 5 - x % 5, grades)
