
array = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print([array[i+1] for i in range(len(array)-1) if array[i]<array[i+1]])
