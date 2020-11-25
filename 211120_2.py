count = list(input('Введите занчения:'))
for i in range(1, len(count), 2):
    count[i - 1], count[i] = count[i], count[i - 1]
print(count)
