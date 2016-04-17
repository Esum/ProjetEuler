
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

def triang(n):
    return (n * (n + 1))//2

def hexa(n):
    return (n * (2*n - 1))


def is_penta(n):
    s = isqrt(24*n + 1)
    if s*s == 24*n + 1:
        return (s + 1)%6 == 0
    return False

def is_triang(n):
    s = isqrt(8*n + 1)
    if s*s == 8*n + 1:
        return (s - 1)%2 == 0
    return False

def is_hexa(n):
    s = isqrt(8*n + 1)
    if s*s == 8*n + 1:
        return (s + 1)%4 == 0
    return False