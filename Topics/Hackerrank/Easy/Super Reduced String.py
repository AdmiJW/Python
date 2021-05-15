
# This is a greedy problem. We shall reduce pairs as soon as possible
#
# As previosuly solved on LeetCode, this problem requires use of stack for efficient reducing
# Since we will reduce essentially any pair ASAP, use of stack enables us to always look for
# the last character, even after popping, allowing us for O(N) time complexity solution


def superReducedString(s):
    stack = []
    for c in s:
        if len(stack) and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)
    return 'Empty String' if len(stack) == 0 else ''.join(stack)
