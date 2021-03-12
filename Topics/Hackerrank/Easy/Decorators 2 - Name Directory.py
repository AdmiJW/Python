
# Here, The name formatter function is provided. Now we simply has
# to decorate the function so that:
#
#   >   The function takes in a list of peoples, which is another array consisting of
#       informations of individual person
#   >   The function will sort the persons prior to formatting names
#
# Here we used decorators. The decorators receive the name formatting function, and returns
# a new function which:
#
#   >   Takes list of persons as parameter, sort them by age.
#   >   Each person will be name formatted via the original name formatting function
#   >   Returns a list which consist of sorted, formatted names
#
#
# Instead of returning full list, we can also chose to return a generator via yield keyword.



# List Solution
def person_lister(f):
    def inner(people):
        people = map(f, sorted(people, key=lambda x: int(x[2] ) ) )
        return people
    return inner


# Generator solution
def person_lister2(f):
    def inner(people):
        for p in sorted(people, key=lambda x: int(x[2] ) ):
            yield f(p)
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == 'M' else 'Ms. ') + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input() ) ) ]
    print(*name_format(people), sep='\n')