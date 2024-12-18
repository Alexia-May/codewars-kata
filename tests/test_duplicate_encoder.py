#Importing the function I will test
from lib.duplicate_encoder import *

#testing with unique letters only in lowercase
def test_unique_letters(): 
    result = duplicate_encoder('python')
    assert result == '(((((('

#testing with a word that contains both unique letters and repeated letters in lowercase
def test_some_unique_some_repeated(): 
    result = duplicate_encoder('alexia')
    assert result == ')(((()'

#testing with a word that contains both unique letters and repeated letters
# With the same letter in lower and upper case

def test_lower_upper():
    result = duplicate_encoder('Anaconda')
    assert result == ')))(()()'

#testing with duplicated and unique non alphanumeric characters
def test_non_alphanumerical():
    result = duplicate_encoder('.(( +')
    assert result == '())(('