

# Brute force O(N^2) time
def icecreamParlor(m, arr):
    for i, val in enumerate(arr):
        for j, val2 in enumerate(arr):
            if i == j or val + val2 != m:
                continue
            return i+1, j+1



# Remember seen values. Uses O(N) extra space for hashmap, but assumed O(N) time
def icecreamParlor(m, arr):
    val_index = {}
    for i, val in enumerate(arr):
        if m - val in val_index:
            return val_index[m-val]+1, i+1
        else:
            val_index[val] = i