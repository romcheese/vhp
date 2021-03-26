
from itertools import permutations

def BiggerGreater(s:str):
    word = []
    for letter in s:
        word.append(letter)

    vars = []

    for i in permutations(s):
        if list(i) > word:
            vars.append(i)

    vars.sort()
    final_word = ''

    try:
        for el in vars[0]:
            final_word += str(el)
    except IndexError:
        return ''

    return final_word

#
#
#
# x = BiggerGreater('fff')
# print(x)
