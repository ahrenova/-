full_data = []
for i in range(100):
    input_user = input('input data: ').strip()
    if input_user == '':
        break
    full_data.append(input_user)
print(full_data)
open_file = open(r'les5_1.txt', 'w' )
for line in full_data:
    open_file.write(f'{line}\n')
open_file.close()



# full_data = []
# input_user = 1
# while input_user != '':
#     input_user = input('input data: ').strip()
#     if input_user != '':
#         full_data.append(input_user)
# print(full_data)

