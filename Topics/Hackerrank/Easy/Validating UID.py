
# This problem simply sepcifies some constraints on the UID allowed:
#   >   At least 2 uppercase English
#   >   At least 3 digits
#   >   Alphanumeric only
#   >   No repeated characters
#   >   Exactly 10 chars
#
# Let's see how can we tackle it
#   >   At least 2 uppercase English:
#           Count the uppercase english characters in UID
#   >   At least 3 digits
#           Count the digits characters in UID
#   >   Alphanumeric only
#           Built in .isalnum() method
#   >   No repeated characters
#           is set() length == 10?
#   >   Exactly 10 chars
#           len()


def soln1():
    for i in range(int(input())):
        UID = input()
        isValid = len(UID) == 10 and UID.isalnum() and len(set(UID)) == 10 and \
                  len(tuple(filter(lambda x: x.isupper(), UID))) >= 2 and \
                  len(tuple(filter(lambda x: x.isdigit(), UID))) >= 3

        print('Valid' if isValid else 'Invalid')


soln1()