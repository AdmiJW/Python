
import re

# Since it already told us the shape of the matrix, I can immediately know the length of the string resulting
# from reading the matrix by columns already.
#
# There is a trick: With the array of size row * col, when reading across a row, the index of the character
# is obtained by
#
#           Row line no + Col line no * total rows
#
# After the complete string is obtained, now we remove those intermediate symbol groups (Non alphanumeric which is
# between 2 alphanumeric characters) by using regex:
#
#   (?<=\w)     Look behind. Matches one alphanumeric character, while doesn't count towards overlapping
#   \W+         Multiple Non-alphanumeric characters
#   (?=\w)      Look ahead. Matches one alphanumeric character, while doesn't count towards overlapping
#
# Replace the matches with single space. That's it!
#
# -----------------------------------------------------------------
#
# Note there is a nice trick of using zip(). For each argument in the zip(), like (1,2), (3,4), it will return
# (1,3), (2,4)
# Therefore if we pass in all the rows as separate arguments, it will return the string read in columns!

def soln1():
    row, col = map(int, input().split() )
    str_arr = [''] * (row * col)

    for r in range(row):
        for c, char in enumerate(input() ):
            index = r + c * row
            str_arr[index] = char

    pattern = re.compile('(?<=\w)\W+(?=\w)')
    print(re.subn( pattern, " ", ''.join(str_arr) ) )

