


if __name__ == '__main__':
    N = int( input() )
    avg_dict = {}

    # Obtain name and list of marks, reduce it to average and store
    # Use * (Destructuring) to automatically retrieve the rest element of a list
    for i in range(N):
        name, *marks = input().split()
        marks = list( map(float, marks) )
        avg_dict[name] = sum(marks) / len(marks)

    # Use of f-string to print in 2 d.p format
    print( f'{ avg_dict[input()]:.2f}' )
