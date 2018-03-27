'''ввести 2 числа. меньшее зпменить полкскммойб большее двойным произведением'''

a = int(input("a = "))
b = int(input("b = "))


if a==b:
    print('они равны')

elif a>b:
    a*=a
    b=(a+b)/2

elif a<b:
    b *= b
    a = (a + b) / 2

print('a=',a,'b=', b)