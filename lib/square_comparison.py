# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number of times it appears). 
# "Same" means, here, 
# that the elements in b are the elements in a squared, regardless of the order.

def b_square_a(a, b):
    print(a)
    print(b)

# Sort
    a = sorted(a)
    b = sorted(b)
    print(a)
    print(b)

#Squaring a
    a_square = list(map(lambda n : n*n, a))
    print(a_square)
    print(b)

# comparing a squared and ordered and b
    if a_square == b and a != []:
        return True
    else:
        return False

