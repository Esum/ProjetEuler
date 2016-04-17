def decomp(n: int, dic=False):
    if dic:
        res = {}
    else:
        res = []
    d = 2
    while n != 1:
        if n%d:
            d += 1
        else:
            if dic:
                if d in res:
                    res[d] += 1
                else:
                    res[d] = 1
            else:                
                res.append(d)
            n //= d
    return res

def isPrime(n: int):
    if n == 0 or n == 1:
        return False
    d = 2
    while d*d <= n:
        if not n%d:
            return False
        d += 1
    return True

primes = lambda min, max: filter(isPrime, range(min, max))

def factors(n: int):
    res = set()
    for i in range(1, n//2 + 1):
        if not n%i:
            res.add(i)
            res.add(n//i)
    return res

def decompsum(n: int, k: int, f=list):
    decomps = [ [ f([]) for j in range(n+1) ] for i in range(k+1) ]
    for j in range(k+1):
        decomps[0][j] = f([f([0] * j)])
    for i in range(1, n+1):
        for j in range(1, k+1):
            for m in range(0, n+1):
                for d in decomps[i-m][j-1]:
                    decomps[i][j].append(f([m] + d))
    return decomps[n][k]

def primesGenerator(lim):
    if lim < 7:
        if lim < 2:
            yield 2
        if lim < 3:
            yield 3
        if lim < 5:
            yield 5

    n = (lim - 1) // 30
    prime1 = [True] * (n + 1)
    prime7 = [True] * (n + 1)
    prime11 = [True] * (n + 1)
    prime13 = [True] * (n + 1)
    prime17 = [True] * (n + 1)
    prime19 = [True] * (n + 1)
    prime23 = [True] * (n + 1)
    prime29 = [True] * (n + 1)
    prime1[0] = False
    i = l = 0
    while l <= n:
        if prime1[i]:
            p = 30 * i + 1
            l = i * (p + 1)
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6
            prime29[l::p] = [False] * (1 + (n - l) // p)
        if prime7[i]:
            p = 30 * i + 7
            l = i * (p + 7) + 1
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 1
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 1
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 1
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime7[l::p] = [False] * (1 + (n - l) // p)
        if prime11[i]:
            p = 30 * i + 11
            l = i * (p + 11) + 4
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 2
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 2
            prime17[l::p] = [False] * (1 + (n - l) // p)
        if prime13[i]:
            p = 30 * i + 13
            l = i * (p + 13) + 5
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 1
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 3
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 3
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 1
            prime23[l::p] = [False] * (1 + (n - l) // p)
        if prime17[i]:
            p = 30 * i + 17
            l = i * (p + 17) + 9
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 3
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 3
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 3
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 3
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime11[l::p] = [False] * (1 + (n - l) // p)
        if prime19[i]:
            p = 30 * i + 19
            l = i * (p + 19) + 12
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 4
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 4
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 2
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 2
            prime23[l::p] = [False] * (1 + (n - l) // p)
        if prime23[i]:
            p = 30 * i + 23
            l = i * (p + 23) + 17
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 5
            prime7[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 5
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 3
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 4
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime17[l::p] = [False] * (1 + (n - l) // p)
        if prime29[i]:
            p = 30 * i + 29
            l = i * (p + 29) + 28
            prime1[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 1
            prime29[l::p] = [False] * (1 + (n - l) // p)
            l += i * 6 + 6
            prime23[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 4
            prime19[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 2
            prime17[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 4
            prime13[l::p] = [False] * (1 + (n - l) // p)
            l += i * 2 + 2
            prime11[l::p] = [False] * (1 + (n - l) // p)
            l += i * 4 + 4
            prime7[l::p] = [False] * (1 + (n - l) // p)
        i += 1
    yield 2
    yield 3
    yield 5
    for i in range(n):
        if prime1[i]: yield 30 * i + 1
        if prime7[i]: yield 30 * i + 7
        if prime11[i]: yield 30 * i + 11
        if prime13[i]: yield 30 * i + 13
        if prime17[i]: yield 30 * i + 17
        if prime19[i]: yield 30 * i + 19
        if prime23[i]: yield 30 * i + 23
        if prime29[i]: yield 30 * i + 29
    if prime1[n] and (30 * n + 1) <= lim: yield 30 * n + 1
    if prime7[n] and (30 * n + 7) <= lim: yield 30 * n + 7
    if prime11[n] and (30 * n + 11) <= lim: yield 30 * n + 11
    if prime13[n] and (30 * n + 13) <= lim: yield 30 * n + 13
    if prime17[n] and (30 * n + 17) <= lim: yield 30 * n + 17
    if prime19[n] and (30 * n + 19) <= lim: yield 30 * n + 19
    if prime23[n] and (30 * n + 23) <= lim: yield 30 * n + 23
    if prime29[n] and (30 * n + 29) <= lim: yield 30 * n + 29