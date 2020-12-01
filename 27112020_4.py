def count_power(number_1, number_2):
    print(number_1**number_2)

number_x=int(input('Pozitive number'))
number_y=int(input('Negative number'))
if number_x>0 and number_y<0:
    count_power(number_x, number_y)
else:
    print('Error')