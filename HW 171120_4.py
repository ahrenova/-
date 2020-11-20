number = int(input('число'))
if number % 2 == 0:
    r = -1
    while number > 10:
        d = number % 10
        number //= 10
        if d > r:
            r = d
    print(r)
else:
    print( 'число нечетное')
