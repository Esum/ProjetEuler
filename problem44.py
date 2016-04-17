from itertools import product

def isqrt(n):
    """
    integer sqrt of n
    """
    c = n*4//3
    d = c.bit_length()

    a = d>>1
    if d&1:
        x = 1 << a
        y = (x + (n >> a)) >> 1
    else:
        x = (3 << a) >> 2
        y = (x + (c >> a)) >> 1

    if x != y:
        x = y
        y = (x + n//x) >> 1
        while y < x:
            x = y
            y = (x + n//x) >> 1
    return x


def penta(n):
    return (n * (3*n - 1))//2


def is_penta(n):
    s = isqrt(24 * n + 1)
    if s*s == 24 * n + 1:
        return (s + 1)%6 ==  0
    return False


def solve44(bound=4000):
    p1 = 0
    p2 = 0
    ecart = bound**2
    for i in range(1, bound+1):
        for j in range(i+1, bound+1):
            a = penta(i)
            b = penta(j)
            if is_penta(a+b):
                if is_penta(abs(a-b)):
                    if abs(a-b) < ecart:
                        ecart = abs(a-b)
                        p1 = a
                        p2 = b
                        print(ecart)
    return ecart
#>>> solve44()
#5482660