
import re


# This checking can be done without regex, or with regex.
# With regex, the checking is done in two parts:
#   1. Check the pattern in general. Whether it is 16 digit, start with 5,6,or 7, and has optional hyphen
#   2. Check for repeating consecutive digits up to 4 times. Any match will result in invalid credit card number

# ^[456]        -   Starts with digit 4,5 or 6
# \d{3}         -   After starting digit, followed by 3 digits
# (-?)          -   Optional hyphen. It is captured
# \d{4}         -   4 digits
# \1            -   After 4 digits, if first captured grp has hyphen, here also need hyphen. Same goes if there is none

# (\d)          -   First digit in attempt repeating consecutive match
# (?:){3}       -   Non capturing group. Repeat 3 times
# -?            -   The digit can followed by a hyphen
# \1            -   First digit captured

def soln1():
    credit_card_pattern = re.compile(r'^[456]\d{3}(-?)\d{4}\1\d{4}\1\d{4}$')
    no_consecutive_pattern = re.compile(r'(\d)(?:-?\1){3}')

    for i in range(int(input() ) ):
        credit_no = input()
        if not re.match(credit_card_pattern, credit_no) or re.search(no_consecutive_pattern, credit_no):
            print("Invalid")
        else:
            print("Valid")
