
if __name__ == '__main__':
    n = int( input().strip() )

    if n % 2 != 0 or n % 2 == 0 and 6 <= n <= 20:
        print('Weird')
    else:
        print('Not Weird')