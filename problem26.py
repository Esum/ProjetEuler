__author__ = 'Benjamin'


import arithm


if __name__ == '__main__':
    res = 1
    max = 1
    for n in arithm.primes(6, 1000):
        i = 1
        while (10**i-1)%n:
            i+=1
        if i>max:
            max = i
            res = n
    print(res)