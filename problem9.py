__author__ = 'Benjamin'

if __name__ == '__main__':
    for a in range(1001):
        for b in range(1001-a):
            if a ** 2 + b ** 2 == (1000 - a - b)**2:
                print(a*b*(1000 - a - b), a, b, (1000 - a - b))
