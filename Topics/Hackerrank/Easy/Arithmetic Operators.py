

if __name__ == '__main__':
    a, b = (int(input() ) for i in range(2) )

    for v in (a+b, a-b, a*b):
        print(v)