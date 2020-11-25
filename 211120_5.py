my_list = [8, 5, 4, 2, 2, 1]
guest = int(input ('Введите натуральное число:'))
for renamber, number in enumerate(my_list):
    if int(guest) < int(number):
        continue
    my_list.insert(renamber, guest)
    break
else:
    my_list.append(guest)
print(my_list)
