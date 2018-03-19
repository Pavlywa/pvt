def summ (n):

    if (n < 10):

        return n

    else:

        return n%10 + summ(n // 10)

print(summ(1928))