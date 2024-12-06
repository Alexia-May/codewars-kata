# Works like a Fibonacci, 
# but summing the last 3 (instead of 2) numbers of the sequence 
# to generate the next.

from lib.tribonacci import *

# n = 0 -> []

#  [1, 1, 1] -> [1, 1 ,1, 3, 5, 9, 17, 31, ...]
def test_1(): 
    result = tribonacci([1, 1, 1], 10)
    assert result == [1, 1, 1, 3, 5, 9, 17, 31, 57, 105]

#  [0, 0, 1] -> [0, 0, 1, 1, 2, 4, 7, 13, 24, ...]
def test_2(): 
    result = tribonacci([0, 0, 1], 9)
    assert result == [0, 0, 1, 1, 2, 4, 7, 13, 24]
