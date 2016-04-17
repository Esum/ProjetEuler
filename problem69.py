

def totient(n):
    facts = factorize(n)
    phi = 1
    for p in facts:
        phi *= (p-1)*p**(facts[p]-1)
    return phi