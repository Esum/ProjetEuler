def sigmas(n):
    s = {1: 1}
    for p in primesGenerator(n):
        q = p
        while q <= n:
            s[q] = (p*q - 1)//(p - 1)
            q *= p
    for k in range(4, n+1):
        if k in s:
            continue
        a = arithm.Brent(k)
        while a != s[a] - 1:
            a = arithm.Brent(a)
        aa = a
        while k % aa == 0:
            aa *= a
        aa //= a
        b = math.gcd(aa, k//aa)
        if b != 1:
            print(k, b)
        s[k] = s[aa]*s[k//aa]
    return s


def propers_sum(n):
    s = sigmas(n)
    return {k: s[k]-k for k in range(1, n+1)}


def chains(n):
    done = set()
    longest_chain = []
    size = -1
    psum = propers_sum(1000000)
    for k in range(1, n+1):
        broken = False
        chain = []
        while not k in chain and k != 0:
            if k in done or k > n:
                broken = True
                break
            chain.append(k)
            k = psum[k]
        if broken:
            continue
        if k != 0:
            if len(chain) - chain.index(k) > size:
                longest_chain = chain
                size = len(chain) - chain.index(k)
    return longest_chain