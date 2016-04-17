import arithm


if __name__ == '__main__':
    n = 1
    piles = 1
    while piles%1000000:
        n += 1
        l = arithm.decompsum(n, n)
        for i in l:
            i = set(i)
        piles = len(l)
    print(n)