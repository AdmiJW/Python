
# Since the input size is small, brute force approach is plausible, in O(N^2) time where N is max len of string
#
# Since the separated number must at least consist of 2 numbers, the first number length must not exceed half size
# of the string. So we attempt numbers up to length N/2
#
# Now we have possible starting numbers. My approach is, to build up the string that we would expect. Since we know
# the length of string, we would keep building until the expected string length exceed or equal the original string
# s (Hopefully, len(s) == len(expected) for matched case)
#
# Say my starting number is 1, and len(s) == 5, then I would build expected string "12345".
# Then, check whether expected string is equal the string s or not. That's it!



def separateNumbers(s):
    for i in range( len(s) // 2 ):
        expected_str = s[:i+1]
        n = int(expected_str) + 1

        while len(expected_str) < len(s):
            expected_str += str(n)
            n += 1
        if expected_str == s:
            return print(f"YES {s[:i+1]}")
    print("NO")
