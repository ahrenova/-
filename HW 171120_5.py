revenue =int(input('Выручка:'))
cost = int(input('Издержки:'))
if(revenue > cost):
    print('прибыль')
else:
    print('убыток')
if(revenue > cost):
    print( 'рентабильность');
    print (str (float(revenue / cost))+'%')
employees= int(input('Численность сотрудников:'))
print ('Прибыль на одного сотрудника:')
print( revenue / employees )


