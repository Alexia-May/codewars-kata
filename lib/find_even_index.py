# Equal Sides Of An Array

# Input
# An integer array of length 0 < arr < 1000. 
# The numbers in the array can be any integer positive or negative.

# Output
# The lowest index N where the side to the left of N is equal to the side to the right of N. 
# If you do not find an index that fits these rules, then you will return -1.

# Note
# If you are given an array with multiple answers, return the lowest correct index.


def find_even_index(arr):
    #making a list of valid n
    valid_n = []
    for n in range(0, len(arr)):
        sum1 = sum(arr[0:n])
        sum2 = sum(arr[n+1:])
        if sum1 == sum2:
            valid_n.append(str(n))
            
    # returning first valid n or -1 if there is no valid n
    if len(valid_n) != 0:
        return int(valid_n[0])
    else:
        return -1
            