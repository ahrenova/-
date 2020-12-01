def division_number(first_number , second_number):
    if second_number != 0:
        print(first_number / second_number)

number_1 = float(input('Enter first number'))
number_2 = float(input('Enter second number'))
division_number(number_1 , number_2)
division_number(number_2 , number_1)