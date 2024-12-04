# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number of times it appears). 
# "Same" means, here, 
# that the elements in b are the elements in a squared, regardless of the order.

def b_square_a(a, b):
    if  type(a) != 'NoneType' and a != None and type(b) != 'NoneType' and b != None : 
        # Squaring a
        a_square = list(map(lambda n : n*n, a))
        # Comparing ordered lists
        return sorted(a_square) == sorted(b)
    else:
        return False

