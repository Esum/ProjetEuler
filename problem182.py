from math import gcd


def diviseurs(n):
    div = set([1, n])
    d = 2
    while d*d <= n:
        if n % d == 0:
            div.add(d)
            div.add(n//d)
        d += 1
    return div
    

def ordres(p=1009, q=3643):
    ordres = {div : 0 for div in diviseurs((p-1) * (q-1))}
    inversibles = set(k for k in range(p*q - 1, 0, -1) if k % p and k % q)
    print(len(inversibles))
    while inversibles:
        n = inversibles.pop()
        print(n)
        cycle = [n]
        while cycle[-1] != 1:
            cycle.append((n * cycle[-1]) % (p * q))
        ordre = len(cycle)
        ordres[ordre] += 1
        for k in range(1, ordre-1):
            if cycle[k] in inversibles:
                ordres[ordre//(gcd(ordre, k))] += 1
                inversibles.discard(cycle[k])
    return ordres