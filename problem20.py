__author__ = 'Benjamin'

if __name__ == '__main__':
    p = 1
    for i in range(1, 101):
        p *= i
    print(sum([int(d) for d in list(str(p))]))