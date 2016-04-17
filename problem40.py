

def log10_int(n):
    lg = 0
    power = 1
    while power <= n:
        lg += 1
        power *= 10
    return lg


def d(n):
    k_nb = 1
    lg = 1
    pos = 1
    for k in range(1, n):
        pos += 1
        if pos > lg:
            k_nb += 1
            lg = log10_int(k_nb)
            pos = 1
    return k_nb, pos

def solve40(indices=[1, 10, 100, 1000, 10000, 100000, 1000000]):
    res = 1
    for nb, pos in map(d, indices):
        res *= int(str(nb)[pos-1])
    return res
#>>> solve40
#210
    