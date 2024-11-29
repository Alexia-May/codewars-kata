# Importing the function I will test
from lib.find_even_index import *

def test_n_middle():
    result = find_even_index([1,2,3,4,5,4,3,2,1])
    assert result == 4

def test_no_n():
    result = find_even_index([1,2,3,4,5,5,4,3,2,1])
    assert result == -1

def test_several_n():
    result = find_even_index([0,0,0,0,0,0,0,0,])
    assert result == 0
