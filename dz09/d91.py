def razvorot (n):

    if (n < 10):

        return n

    else:

        print(n%10)

        return razvorot(n // 10)

print(razvorot(1234))