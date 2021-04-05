

# Approach 1: Slicing and joining
def mutate_string(string, position, character):
    return string[:position] + character + string[position+2:]


# Approach 1.1: Without using + operator, use format instead
def mutate_string2(string, position, character):
    return f"{string[:position]}{character}{string[position+1:]}"

# Approach 2: Split string into list, mutate list, join back
def mutate_string3(string, position, character):
    split = [*string]
    split[position] = character
    return "".join(split)