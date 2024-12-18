# The goal of this exercise is to convert a string to a new string where 
# each character in the new string is "(" if that character appears only once in the original string, 
# or ")" if that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a duplicate.

def duplicate_encoder(word):
    word = word.lower()
    code = []
    list_word = list(word)
    for letter in list_word:
        if list_word.count(letter) > 1:
            code.append(')') 
        else: 
            code.append('(')
    return ''.join(code)
