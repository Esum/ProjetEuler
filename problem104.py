from decimal import *


def is_pand(n, to=9):
    d = list(str(n))
    if len(d) != to:
        return False
    d.sort()
    return d == [str(k) for k in range(1, len(d)+1)]

def fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        f1, f2 = 1, 1
        for k in range(n-2):
            f1, f2 = f1 + f2, f1
        return f1

def fibo_mod(n, m=1000000000):
    if n == 1 or n == 2:
        return 1
    else:
        f1, f2 = 1, 1
        for k in range(n-2):
            f1, f2 = (f1 + f2) % m, f1
        return f1

def solve104():
    k = 2749
    phi = (Decimal(1) + Decimal(5)**(Decimal(1)/Decimal(2))) / Decimal(2)
    f_deb = phi**(2749) / (Decimal(5)**(Decimal(1)/Decimal(2)))
    f1, f2 = 2250249, 768327376
    while True:
        if is_pand(f1):
            s = str(f_deb)
            s = s[0]+s[2:10]
            print(k)
            print(s)
            if is_pand(int(s)):
                return k
        f_deb *= phi
        f1, f2 = (f1 + f2) % 1000000000, f1
        k += 1
