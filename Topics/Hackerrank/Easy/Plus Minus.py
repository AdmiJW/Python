# Count the number of positives, negatives and zero. Then divide by the length of array
# to obtain final result
# Alternatively, add 1/len to corresponding variable for each value

# Of course you can count positive, negative and zero separately, and it requires 3 iterations.


def plusMinus(arr):
    pos, neg, zero, inc = 0, 0, 0, 1 / len(arr)
    for v in arr:
        if v == 0:
            zero += inc
        elif v < 0:
            neg += inc
        else:
            pos += inc
    print(f'{pos:.4f}\n{neg:.4f}\n{zero:.4f}')
