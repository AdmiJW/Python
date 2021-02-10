
import re

# Filter is a higher order function which for every element in iterables, will pass into a boolean returning
# function. If False, the element will be filtered out, not exist anymore in the final list


# Regex Solution
def soln1():
    emailRegex = re.compile( "^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$")
    emails = [ input() for i in range( int(input() ) ]
    print( *sorted( filter( lambda x: re.fullmatch(emailRegex, x) ) ) )


# Since email can be split into 3 parts, just split it.
def soln2():
    # Split on @, check if it is split into 2 parts only
    # Split on ., check if it is split into 3 total parts
    # Check last token's length if it is 3
    # No empty strings allowed.
    def isEmail(e: str):
        parts = e.split('@')
        if len(parts) != 2: return False
        parts = [parts[0], *parts[1].split('.') ]
        if len(parts) != 3 or len(parts[2]) > 3: return False
        return parts[0].replace('-','').replace('_','').isalnum() and parts[1].isalnum() \
               and parts[2].isalpha()


    # Better code using Exception Handling and Replacing characters so isalnum() can be used
    def isEmail2(e: str):
        try:
            user, comp = e.split('@')
            comp, ext = comp.split('.')
        except ValueError:
            return False
        return user.replace('-', '').replace('_', '').isalnum() and comp.isalnum() and len(ext) <= 3 and ext.isalpha()

    emails = [ input() for i in range(int(input() ) ) ]
    print( *sorted( filter( isEmail, emails ) ) )