

# What is Standard Deviation?
#
#   A standard deviation, put simply, is the SQUARE ROOT of AVERAGE of THE DISTANCE OF EACH ELEMENT
#   FROM THE MEAN, SQUARED
#
#   To put step by step, how would we really describe how spread out a dataset is from each other?
#   Maybe we measure spread by the distance of the data from the mean? OK
#
#   We can find average of each data from mean directly, by using
#               x - u       ( u is the mean )
#               -----
#                 n
#
#   However, for negative numbers like -2,-1,0,1,2. The answer would be 0, which is incorrect
#   This is because of the negative numbers. Mean is 0, and the sum would just be 0 before dividing N!
#
#   To alleviate this, the distances must be somehow always positive. There's no such thing as negative
#   distance!
#
#   One way is to absolute the distance calculated ( | | ). However, this is hard to manipulate algebraically.
#   Thus, mathematicians use another way: Square each of distance, (Now its called VARIANCE), then at the
#   end, square root it (Standard Deviation)


N = int(input() )
arr = [ int(i) for i in input().split() ]

# Obtain mean
mean = sum(arr) / N

# Calculate each element's distance from mean, squared. THen, Sum them, find average, then square root
dist_squared = [ (i - mean) ** 2 for i in arr ]
print( '{:.1f'.format( ( sum(dist_squared) / 2 ) ** 0.5 ) )