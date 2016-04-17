
def log10_int(n):
    lg = 0
    power = 1
    while power <= n:
        lg += 1
        power *= 10
    return lg

def is_pand(n):
    d = list(str(n))
    d.sort()
    return d == [str(k) for k in range(1, len(d)+1)]

def solve41(n=1000000):
    pand = 0
    for p in primesGenerator(n):
        if is_pand(p):
            pand = p
    return pand
#>>> solve41()
#7652413