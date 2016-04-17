import math


if __name__ == '__main__':
    summ = 0
    fact = [math.factorial(k) for k in range(10)]
    for k in range(3, 400000):
        d = [int(c) for c in list(str(k))]
        if k == sum(fact[c] for c in d):
            summ += k