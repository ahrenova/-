def int_func(word):
    # print(word.capitalize())
    return word.capitalize()

# int_func('text')
# print(int_func('tEXt'))
words = input('Enetr words use space:')
for word in words.split():
    print(int_func(word),end=' ')

