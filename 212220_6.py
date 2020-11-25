Chocolate = []
data = {'Название': '', 'Цена': '', 'Количество': '',  'еденица измерения': ''}
data_2 = {'Название': [], 'Цена': [], 'Количество': [],  'еденица измерения': []}
num = 0
while True:
    if input('Выход - Q, \nЛюбая клаиша - продолжить:').upper() == 'Q':
        break
    num +=1
    for f in data.keys():
        user = input(f'{f}: ')
        data[f] = int(user) if (f == 'цена' or f == 'количества') else user
        data_2[f].append(data[f])
    Chocolate.append((num, data.copy()))
    print('Базовые данные:\n')
    for key, value in data_2.items():
        print(key, value)