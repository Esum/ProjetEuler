def repetend(p, b=10):
    length = 1
    k = b
    while k != 1:
        k = (k * b) % p
        length += 1
    n = (b**(p-1) - 1) // p
    return n % (10**length), length


def repetend_length(p, b=10):
    orders = list(arithm.factors(p - 1))
    orders.sort()
    for order in orders:
        if pow(b, order, p) == 1:
            return order


def solve133(lim=100000):
    pfac = set()
    for p in primesGenerator(lim):
        if p == 2 or p == 3 or p == 5:
            pfac.add(p)
            continue
        length = repetend_length(p)
        if any(f != 2 and f != 5 for f in arithm.factorize(length).keys()):
            pfac.add(p)
    return sum(pfac)