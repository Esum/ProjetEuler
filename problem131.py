import random


def is_perfect_cube(n):
    low = 2
    high = n
    while high - low > 1:
        mid = low + ((high - low) >> 1)
        k = mid*mid*mid
        if k  < n:
            low = mid
        elif k > n:
            high = mid
        else:
            return  True
    if low*low*low == n:
        return True
    return False


def cuberoot(a, p):
    if p == 2:
        return a
    if p == 3:
        return a
    if p % 3 == 2:
        return pow(a, (p+p - 1) // 3, p)
    elif p % 9 == 4:
        root = pow(a, (p+p + 1) //9, p)
        if pow(root,3,p) == a % p:
            return root
    elif p % 9 == 7:
        root = pow(a, (p + 2) // 9, p)
        if pow(root, 3, p) == a % p:
            return root
    else:
        s = 0
        t = p - 1
        while t % 3 == 0:
            t //= 3
            s += 1
        k = t // 3
        if t % 3 == 2:
            k += 1
        b = arithm.modinv(9, p)
        c = pow(b, t, p)
        r = pow(a, t, p)
        h = 1
        cc = pow(c, 3**(s - 1), p)
        c = arithm.modinv(c, p)
        for i in range(1, s):
            d = pow(r, 3**(s - i - 1), p)
            if d == cc:
                h = (h * c) % p
                r = (r * c*c*c) % p
            elif d != 1:
                l = (c*c) % p
                h = (h * l) % p
                r = (r * l*l*l) % p
            c = (c*c*c) % p
        r = (pow(a, k, p) * h) % p
        if t % 3 == 1:
            return arithm.modinv(r, p)
        else:
            return r

def solve131(maxp=1000000, lim=1000000, nlim=10000):
    primes = set()
    for p in primesGenerator(lim):
        for n in range(1, nlim):
            if is_perfect_cube(n*n*n + n*n*p):
                primes.add(p)
                print(primes)
                break
    return primes
                    