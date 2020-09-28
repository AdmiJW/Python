import numpy as np
from typing import *


def calculate( arrlist: List) -> Dict:

    #   Invalid 3x3 Matrix. Raise an Error for that
    if ( len( arrlist ) != 9 ):
        raise ValueError("List must contain nine numbers.")

    #   Create a numpy Array and reshape to the correct 3x3 dimension
    matrix:np.ndarray = np.array( arrlist ).reshape( (3,3) )

    #   The result dictionary.
    #   It will be in the following structure:
    #   {
    #       'mean': [ [...], [...], x ],
    #       'variance': [ [...], [...], x ],
    #       'standard deviation': [ [...], [...], x ],
    #       'max': [ [...], [...], x ],
    #       'min': [ [...], [...], x ],
    #       'sum': [ [...], [...], x ]
    #   }
    #
    result:Dict = dict()

    #   Mean
    mean = result['mean'] = list()
    mean.append( matrix.mean( axis=0).tolist() )
    mean.append( matrix.mean( axis=1).tolist() )
    mean.append( matrix.mean() )

    #   Variance
    variance = result['variance'] = list()
    variance.append( matrix.var( axis=0).tolist() )
    variance.append( matrix.var( axis=1).tolist() )
    variance.append( matrix.var() )

    #   Standard Deviation
    std_dev = result['standard deviation'] = list()
    std_dev.append( matrix.std( axis=0).tolist() )
    std_dev.append( matrix.std( axis=1).tolist() )
    std_dev.append( matrix.std() )

    #   Max
    mat_max = result['max'] = []
    mat_max.append( matrix.max( axis=0).tolist() )
    mat_max.append( matrix.max( axis=1).tolist() )
    mat_max.append( matrix.max() )

    #   Min
    mat_min = result['min'] = []
    mat_min.append( matrix.min( axis=0).tolist() )
    mat_min.append( matrix.min( axis=1).tolist() )
    mat_min.append( matrix.min() )

    #   Sum
    mat_sum = result['sum'] = []
    mat_sum.append( list( matrix.sum( axis=0) ) )
    mat_sum.append( list( matrix.sum( axis=1) ) )
    mat_sum.append( matrix.sum() )

    return result