from typing import *

################################################
# Using List to Keep Track of Alphabets Solution
################################################
def print_rangoli(size:int) -> None:
    char_list = [ chr(size - 1 + ord('a') ) ]      # The list that we use to store one row of alphabet characters,
                                                   # like [b,a,b]
    max_chars = size * 2 - 1                       # The maximum no of characters that will exist. Every character
                                                   # will occur 2 times except the middle one
    max_len = max_chars * 2 - 1                    # The maximum length of the characters joined with -, excluding the
                                                   # prefixing and suffixing dashes -. Every character will be followed
                                                   # by a dash, except the last one

    # Perform printing for expanding part
    for i in range(size):
        len_covered = len(char_list) * 2 - 1            # Length covered by the current characters in this row
        dash_toprint = (max_len - len_covered) // 2     # Number of dashes to print in suffix and prefix

        print( '-' * dash_toprint, '-'.join(char_list), '-' * dash_toprint , sep='')    # Using string multiplication

        expand_char_list(char_list)

    shrink_char_list(char_list)         # At the end, it will over expand by one time. Shrink it first

    # Perform printing for shrinking part
    for i in range(size - 1):
        shrink_char_list(char_list)
        len_covered = len(char_list) * 2 - 1            # Length covered by the current characters in this row
        dash_toprint = (max_len - len_covered) // 2     # Number of dashes to print in suffix and prefix

        print( '-' * dash_toprint, '-'.join(char_list), '-' * dash_toprint, sep='')


# Expands the character list with the one lower topological character
def expand_char_list(char_list: List) -> None:
    mid = len(char_list) // 2
    curr_char = char_list[mid]
    char_list.insert(mid, curr_char)                        # Append the duplication of middle element first
    char_list.insert(mid + 1, chr( ord(curr_char) - 1) )    # Append the lower topological element in middle


# Shrinks the character list by removing the middle element
def shrink_char_list(char_list: List) -> None:
    mid = len(char_list) // 2
    char_list.pop(mid)      # Remove middle single element
    char_list.pop(mid)      # Remove the duplicated element which will be next single element


#########################################################
# Using list of alphabets and indexing substring Solution
#########################################################
import string

def print_rangoli2(size: int) -> None:
    alphabets = string.ascii_lowercase[:size][::-1]    # Obtain the alphabets in scope, reversed order

    for i in range(1, size + 1):
        print('-' * (2 * (size - i) ),                               # Prefixing dashes. No of dashes to print is 2(size - i)
              '-'.join( alphabets[ : i] + alphabets[:i-1][::-1] ),   # The alphabets.
              '-' * (2 * (size - i) ), sep='')                       # Suffixing dashes

    for i in range(size - 1, 0, -1):
        print('-' * (2 * (size - i) ),
              '-'.join(alphabets[: i] + alphabets[:i - 1][::-1]),
              '-' * (2 * (size - i) ), sep='')


def print_rangoli3(size: int) -> None:
    alphabets = string.ascii_lowercase[:size][::-1]         # Obtain the alphabets in scope, reversed order
    li = []

    for i in range(1, size + 1):
        # Use of str.center() to center the middle part of characters in fixed width, padded with '-'
        li.append( '-'.join( alphabets[:i] + alphabets[:i-1][::-1] ).center(4*size - 3, '-') )

    [ print(s) for s in li+li[-2::-1] ]     # Use of list comprehension to print the list.
                                            # Iterate over the list first, then reverse iteration without last row


