__author__ = 'Benjamin'


if __name__ == '__main__':
    max_a = 0
    max_b = 0
    primes = 0
    for a in range(-1000,1000):
        for b in range(-1000,1000):
            n = 0
            while is_prime(n*n + a*n + b):
                n += 1
            if n>primes:
                max_a = a
                max_b = b
                primes = n
                print(primes, a, b)
    print(max_a * max_b)
