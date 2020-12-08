sum_salary = 0
for line in open('lesson5_3.txt').readlines():
    data_user = line.split()
    if float(data_user[1])<20000:
        print(data_user[0])
    sum_salary +=float(data_user[1])
count_emp = len(open('lesson5_3.txt').readlines())
print(int(sum_salary/count_emp))