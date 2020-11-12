

# Read user input
N = int(input() )
elems = list( int(i) for i in input().split() )
weights = list( int(i) for i in input().split() )

# Calculate weighted mean
weighted_mean = sum( elems[i] * weights[i] for i in range(N) ) / sum( weights )

print( '{:.1f}'.format(weighted_mean) )
