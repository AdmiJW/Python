
import collections
import math

# Obtaining the input from the user input
N = int( input() )
arr = list( int(i) for i in input().split() )

# MEAN
print( '{:.1f}'.format( sum( arr ) / len( arr ) ) )


# MEDIAN
medianPoint = math.ceil( len(arr ) / 2 ) - 1
median = sorted( arr )[ medianPoint: medianPoint + (1 if len(arr) % 2 else 2) ]
print( '{:.1f}'.format( sum(median) / len(median) ) )


# MODE
# Use of collections.Counter to count occurrences
freqTable = collections.Counter( arr ).most_common()
mode = list( filter( lambda x: x[1] == freqTable[0][1], freqTable ) )
print( min( i[0] for i in mode ) )
