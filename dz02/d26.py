print ('calculator')

n = int (input('number 1: '))
m = int (input('number 2: '))
v = input('what action? \n 1 + \n 2 - \n 3 \ \n 4 * \n')
if v == '1':
    r = n + m
    print('result= ', r)
elif v == '2':
    r = n - m
    print('result= ', r)
elif v == '3':
    r = float(n / m)
    print('result= ', r)
elif v == '4':
    r = n * m
    print('result= ',r)
else:
    print('result nan')