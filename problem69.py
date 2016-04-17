from arithm import decomp


def totient(n):
    facts = decomp(n, True)
    phi = 1
    for p in facts:
        phi *= (p-1)*p**(facts[p]-1)
    return phi