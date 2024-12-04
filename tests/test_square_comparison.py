# Given two arrays a and b write a function comp(a, b) (orcompSame(a, b)) 
# that checks whether the two arrays have the "same" elements, 
# with the same multiplicities (the multiplicity of a member is the number of times it appears). 
# "Same" means, here, 
# that the elements in b are the elements in a squared, regardless of the order.

from lib.square_comparison import *

# Test b = a square, both lists are in the same order -> True
def test_same_ordered():
    a = [24, 19, 8, 30, 2, 6]
    b = [576, 361, 64, 900, 4, 36]
    result = b_square_a(a, b)
    assert result == True

# Test b = a square, the lists are in different orders -> True
def test_same_unordered():
    a = [24, 19, 8, 30, 2, 6]
    b = [900, 4, 36, 64, 361, 576]
    result = b_square_a(a, b)
    assert result == True

# b does not contain any sqaure of a -> False
def test_same_length_different():
    a = [24, 19, 8, 30, 2, 6]
    b = [3, 35, 67, 362, 528]
    result = b_square_a(a, b)
    assert result == False

#b contains some square of a and no other numbers -> False
def test_some_same():
    a = [24, 19, 8, 30, 2, 6]
    b = [4, 36, 64]
    result = b_square_a(a, b)
    assert result == False

#b contains some square of a and some other numbers -> False
def test_some_same_some_different():
    a = [24, 19, 8, 30, 2, 6]
    b = [4, 36, 64, 3, 35, 61]
    result = b_square_a(a, b)
    assert result == False

#b contains all square of a and some other numbers -> False
def test_same_plus_different():
    a = [24, 19, 8, 30, 2, 6]
    b = [4, 36, 64, 361, 526, 5, 6, 7, 8, 9, 10]
    result = b_square_a(a, b)
    assert result == False

# a is null -> False
def test_a_null():
    a = []
    b = [4, 36, 64, 361, 526, 5, 6, 7, 8, 9, 10]
    result = b_square_a(a, b)
    assert result == False

#b is null -> False
def test_b_null():
    a = [24, 19, 8, 30, 2, 6]
    b = []
    result = b_square_a(a, b)
    assert result == False

#Both a and b are null -> False
def test_a_b_null():
    a = []
    b = []
    result = b_square_a(a, b)
    assert result == True

