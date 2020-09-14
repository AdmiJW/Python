from typing import List

#   The function used in map function. Takes in a string representing one single arithmetic problem:
#       Returns the error message if the arithmetic problem is invalid
#       Else it will return a list where indices:
#           0:  The first operand (str)
#           1:  The operator (str)
#           2:  The second operand (str)
#           3:  The spaces that should be allocated for printing (including the operand)
#           4:  The answer to arithmetic problem
def problem_reducer(problem: str):
    splitted = problem.split()

    #   Error case: The operand is not + or -
    if splitted[1] != '+' and splitted[1] != '-':
        return "Error: Operator must be '+' or '-'."
    #   Error case: The amount of characters exceeded 4
    if len(splitted[0]) > 4 or len(splitted[2]) > 4:
        return 'Error: Numbers cannot be more than 4 digits.'
    #   Append the space that will be taken up by this arithmetic problem
    splitted.append( max(len(splitted[0]), len(splitted[2] ) ) + 2 )
    #   Append the answer to the arithmetic operation
    try:
        splitted.append( str(int(splitted[0]) + int(splitted[2]) if splitted[1] == '+'
                         else int(splitted[0]) - int(splitted[2]) ) )
    #   Error case: The numbers cannot be parsed into int; It contains invalid characters
    except Exception:
        return 'Error: Numbers must only contain digits.'

    return splitted



def arithmetic_arranger(problems: List, answer: bool=False):
    #   Error case: The amount of problems exceed 5
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #   Apply the mapping function
    problems = list( map( problem_reducer, problems) )
    #   Check for invalid cases (Error messages). If there is, just return Error message
    for i in problems:
        if (type(i) == str):
            return i

    res = ''

    #   First line: Print n spaces where n = spaceTaken - len(operand1), then print operand1
    for prob in problems:
        res += (' ' * ( prob[3] - len(prob[0]) ) + prob[0] + '    ' )
    res = res.rstrip()
    res += '\n'

    #   Second Line: Print operand first, then n spaces where n = spaceTaken - 1 - len(operand2), then print operand2
    for prob in problems:
        res += (prob[1] + ' ' * ( prob[3] - 1 - len(prob[2]) ) + prob[2] + '    ')
    res = res.rstrip()
    res += '\n'

    #   Third Line: Print dashes (spaceTaken) times
    for prob in problems:
        res += ('-' * prob[3] + '    ')
    res = res.rstrip()
    res += '\n'

    #   Fourth Line (If true): Print n spaces first where n = spaceTaken - len(ans), then print ans
    if answer:
        for prob in problems:
            res += (' ' * ( prob[3] - len(prob[4] ) ) + prob[4] + '    ' )
    res = res.rstrip()
    return res



li = ["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]
mystr = arithmetic_arranger( li, True )
print(mystr)
print(mystr.encode() )
