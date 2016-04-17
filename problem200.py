from itertools import product


def squbes(lim):
    sqube = set()
    for p in primesGenerator(lim):
        for q in primesGenerator(lim):
            if p == q:
                continue
            sqube.add(p**2 * q**3)
    return sqube

def is_prime_proof(n):
    s = str(n)
    for k in range(0, len(s)-1):
        for d in range(10):
            if is_prime(int((s[:k] + str(d) + s[k+1:]))):
                return False
    for d in [1, 3, 7, 9]:
        if is_prime(int(s[:-1] + str(d))):
            return False
    return True
            