offer = input('Предложение:')
part = offer.split()
for i, word in enumerate(part):
    print(i, word[ : 10])
