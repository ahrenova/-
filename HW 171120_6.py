firstday = int(input('Первый день'))
finish = int(input('Конечный результат'))
day = 1
while finish - firstday > 0:
    firstday = firstday + (firstday * 0.1)
    day += 1
print(day)



