# Importing the function I will test
from lib.delete_nth import *

def test_2_is_enough():
    result = delete_nth([1,2,3,1,2,1,2,3], 2)
    assert result == [1,2,3,1,2,3]

def rest_1_is_enough():
    result = delete_nth([20,37,20,21], 1)
    assert result == [20,37,21]