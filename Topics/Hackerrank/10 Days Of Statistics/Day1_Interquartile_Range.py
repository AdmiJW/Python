from typing import *
from collections import OrderedDict


# Pass in an supposedly ordered Dictionary which maps: Element -> Weight
# And pass in the start and end, the range of weights to search for.
# Will try and find the median value back
def get_median_weighted( dic: Dict, start: int, end: int ) -> float:
    length: int = end - start + 1
    midCount: int = start + (length + 1) // 2
    keys = tuple( dic.keys() )
    idx: int = 0

    while dic[ keys[idx] ] < midCount:
        idx += 1

    if length % 2 == 0 and dic[ keys[idx] ] < midCount + 1:
        return (keys[idx] + keys[idx + 1]) / 2
    return keys[idx]


# Obtain the input
N: int = int(input() )
elem: List = [ int(i) for i in input().split() ]
freq: List = [ int(i) for i in input().split() ]


# First obtain the dictionary where elem maps to its weight. Then, obtain sorted key list.
# Then replace the dictionary with an orderedDict which keys are in sorted order
# ### An alternative way would be to use a nested List
dic = dict( zip(elem, freq) )
sortd = sorted(elem)
dic = OrderedDict( { sortd[idx]: dic[sortd[idx]] for idx in range(len(elem) ) } )

# Transform the dictionary into a Cumulative frequency table
cumulative = 0              # This variable, at the end of loop, will be sum of the weights
for k,v in dic.items():
    cumulative += v
    dic[k] = cumulative

# Obtain the mid point to allow split into Q1 and Q3 easily
midPoint: int = (cumulative - 1) // 2

# Find the Q1 and Q3
firstQ = get_median_weighted(dic, 0, midPoint if cumulative % 2 == 0 else midPoint - 1)
thirdQ = get_median_weighted(dic, midPoint + 1, cumulative - 1)

print( '{:.1f}'.format(thirdQ - firstQ ) )