



if __name__ == '__main__':
    N = int( input() )
    namelist = [ [ input(), float( input() ) ] for i in range(N) ]

    # Find the minimum score
    min_score = min( namelist, key=lambda x: x[1] )[1]

    # Use the loop to find the second minimum score
    second_min = float('inf')
    res = []
    for name in namelist:
        # Found a new minimum. Clear the previous names and update
        if name[1] < second_min and name[1] > min_score:
            res.clear()
            second_min = name[1]
        # If current student mark is equal to second min, append his name
        if name[1] == second_min:
            res.append(name[0])

    # Print the names using list comprehension
    [ print(i) for i in sorted(res) ]


    #################################
    # ALTERNATIVE: Using Sets to sort
    #################################
    scoreset = set(namelist)
    res = sorted( [student[0] for student in namelist if student[1] == sorted(scoreset)[1] ] )

    print( '\n'.join( sorted(res) ) )