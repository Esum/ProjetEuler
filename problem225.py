def tribonacci_mod(n, m):
    if 1 <= n <= 3:
        return 1
    else:
        f = [1, 1, 1]
        for k in range(n-3):
            f.append((f[-1] + f[-2] + f[-3]) % m)
        return f

def solve225(lim=100):
    order = 1
    k = 29
    while order < 124:
        f1 = f2 = f3 = 1
        for i in range(lim*k-3):
            f1, f2, f3 = (f1 + f2 + f3) % k, f1, f2
            if f1 == 0:
                break
        if f1 != 0:
            order += 1
        k += 2
    return k - 2