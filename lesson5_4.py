new_data = []
for line in open('lesson5_4.txt').readlines():
    print(line.split())
    line_array = line.split()
    if line_array[0]=='One':
        new_data.append(f'Один {line_array[1]} {line_array[2]}\n')
    new_data.append(line.replace('Two','Два'))
    new_data.append(line.replace('Three','Три'))
    new_data.append(line.replace('Four','Четыре'))
print(new_data)
open_file = open(r'les5_4new.txt', 'w',encoding='UTF-8' )
for line in new_data:
    open_file.write(line)
open_file.close()