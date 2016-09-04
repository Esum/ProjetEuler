def repetend(p, b=10):
    length = 1
    k = b
    while k != 1:
        k = (k * b) % p
        length += 1
    n = (b**(p-1) - 1) // p
    repetend = str(n)
    return int(repetend[-length:]), length


def repetend_length(p, b=10):
    length = 1
    k = b
    while k != 1:
        k = (k * b) % p
        length += 1
    return length
    

def solve132(rep=1000000000, number=40, lim=18453761):
    pfac = set()
    for p in primesGenerator(lim):
        if p == 2 or p == 3 or p == 5:
            continue
        length = repetend_length(p)
        if rep % length == 0:
            pfac.add(p)
            print(p)
        if len(pfac) == number:
            return sum(pfac)