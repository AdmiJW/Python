

# First, From z-table, Z = 1.96 maps to P(X < Z) = .97500, meaning 97.5%
# Since normal distribution is symmetry around the mean, Area to left of Z = -1.96 is 2.5%
# Taking those away, we will get 95% in middle

# Formula of the Z score to X value:
#          Z = ( x - u ) / sd
# Then to find the x,
#           x = Z * sd + u

# Since mentioned it is SAMPLE MEAN, not SAMPLE SUM,
#       new mean = old mean
#       new std = sqrt( N ) * old std



if __name__ == '__main__':
    sample_size = int( input() )
    mean = float( input() )
    std_dev = float( input() )
    percentage = float( input() )
    z_value = float( input() )

    new_mean = mean
    new_std_dev = std_dev / (sample_size ** 0.5)

    print('{:.2f}'.format( (-z_value) * new_std_dev + new_mean ) )
    print('{:.2f}'.format( z_value * new_std_dev + new_mean) )

