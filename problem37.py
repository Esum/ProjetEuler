from arithm import primesGenerator, isPrime


def to_10(l):
    return sum([l[k]*10**k for k in range(len(l))])


if __name__ == '__main__':
    trunc = [2, 3, 5, 7]
    for p in primesGenerator(100000):
        if p <= 7:
            continue
        d = [int(c) for c in list(str(p))][-1::-1]
        is_trunc = True
        for k in range(1, len(d)-1):
            n = to_10(d[:k])
            print(n)
            if not isPrime(n):
                is_trunc = False
                break
            n = to_10(d[k:])
            if not isPrime(n):
                is_trunc = False
                break
        if is_trunc:
            trunc.append(p)
    print(trunc)