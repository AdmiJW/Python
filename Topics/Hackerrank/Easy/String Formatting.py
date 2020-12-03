

def print_formatted(number):
    # Converted string include the 0b, thus minus that length
    padding = len(bin(number)) - 2

    # Since padding is variable, the format string is done beforehand for easier use
    # This requires the string formatting prerequisite to know padding, and number base representation
    format_str = f'{{:>{padding}}} {{:>{padding}o}} {{:>{padding}X}} {{:>{padding}b}}'
    for i in range(1, number + 1):
        # Format the string only after
        print(format_str.format(i, i, i, i))


def print_formatted2(number):
    padding = len(bin(number)) - 2

    # Step-by-step method, padding is done by rjust() method on strings, and conversion is done by oct(), hex(), bin()
    for i in range(1, number + 1):
        deci = str(i).rjust(padding)
        octa = oct(i)[2:].rjust(padding)
        hexa = hex(i)[2:].upper().rjust(padding)
        binary = bin(i)[2:].rjust(padding)

        print(deci, octa, hexa, binary)


def print_formatted3(number):
    padding = len(bin(number)) - 2

    # Use of nested string formatting, differentiated by indexing and key names. Padding is the key, and 0 means
    # the index of the argument of format()
    for i in range(1, number + 1):
        print( '{0:{padding}} {0:{padding}o} {0:{padding}X} {0:{padding}b}'.format(i, padding) )


if __name__ == '__main__':
    N = int( input() )
    print_formatted(N)
