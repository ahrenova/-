def get_sum(start_sum):
    for i in range(100):
        numbers = input('Enter Number use space')
        # if numbers == 'a':
        #     break
        # print(numbers)
        # print(numbers.split())
        for number in numbers.split():
            if number == 'a':
                break
            sum_number += float(number)
        if number == 'a':
            break
        print(sum_number)

sum_number = 0
get_sum(sum_number)
print(sum_number)
