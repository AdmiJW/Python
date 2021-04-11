
# Thanks to python having built in text alignment methods, we don't have to do much
# dirty work ourselves
#
# The problem is split into 3 parts: Upper, mid and Lower
# Notice the pattern of each row is:
#       >   the middle part is '.|.', which occur 1,3,5,7,9... times
#           Therefore use odd number formula with row number to obtain the result
#           Use .center() to pad the string up to M width!
#       >   The center row is simply 'WELCOME' centered to width M
#       >   The lower part is upper part's reversed.



def soln1():
    N, M = map(int, input().split() )

    # Upper part
    for i in range(N // 2):
        print( (".|."*(i*2 + 1) ).center(M, '-') )
    # Middle
    print('WELCOME'.center(M, '-') )
    # Lower part. If you keep the upper part in list, you can use [::-1]
    for i in range(N // 2 - 1, -1, -1):
        print( (".|." * (i * 2 + 1)).center(M, '-'))
