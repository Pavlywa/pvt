a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a>=b>=c:
    a *= 2
    b *= 2
    c *= 2
    print(a, b, c)

else:
    buf = a
    a = b
    b = buf
    print(a, b, c)