from fractions import *


if __name__ == '__main__':
    
    frac = []
    for k in range(1, 10):
        for l in range(1, 10):
            for m in range(1, 10):
                for n in range(1, 10):
                    num = k*10 + l
                    denom = m*10 + n
                    f = num/denom
                    if f >= 1:
                        continue
                    if l == n and f == k/m:
                        frac.append(Fraction(k, m))
                        print(num, denom)
                    if l == m and f == k/n:
                        frac.append(Fraction(k, n))
                        print(num, denom)
                    if k == n and f == l/m:
                        frac.append(Fraction(l, m))
                        print(num, denom)
                    if k == m and f == l/n:
                        frac.append(Fraction(l, n))
                        print(num, denom)
    print(frac)