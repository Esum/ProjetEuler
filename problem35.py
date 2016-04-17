from arithm import primesGenerator, isPrime


if __name__ == '__main__':
    circ = []
    for p in primesGenerator(1000000):
        d = [int(c) for c in list(str(p))][-1::-1]
        is_circ = True
        for k in range(1, len(d)):
            e = [0]*len(d)
            for c in range(len(d)):
                e[c] = d[(c + k) % len(d)]
            if not isPrime(sum(e[c]*10**c for c in range(len(d)))):
                is_circ = False
                break
        if is_circ:
            circ.append(p)
    print(circ)