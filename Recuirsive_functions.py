def calc_fac(n):
    pass
    if n == 1:
        return 1
    else:
        return n * calc_fac(n-1)


def fibo(n):
    if n < 2:
        return n

    else:
        return fibo(n-1) + fibo(n-2)


def sum_num(a, b):
    if b == 0:
        return a
    else:
        return sum_num(a, b-1) + 1


def multi_num(a, b):
    if b == 0:
        return 0
    else:
        return multi_num(a, b-1) + a


def divi(a, b):
    if a < b:
        return 0
    else:
        return divi(a-b, b) + 1


# Hannoi Tower
def Hannoi(n, A, B, C):
    if n == (1):
        print(A, 'to', C)
    else:
        Hannoi(n-1, A, C, B)
        print(A, 'to', C)
        Hannoi(n-1, B, A, C)
