from functools import reduce

def custom_sum(first, second):
    return first * second

print(reduce(custom_sum, (i for i in range(100, 1001,2))))