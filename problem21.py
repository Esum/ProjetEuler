__author__ = 'Benjamin'

import arithm


if __name__ == '__main__':
    res = 0
    for i in range(1, 10000):
        n = sum(arithm.factors(i))
        if n != i:
            if sum(arithm.factors(n)) == i:
                res += n
    print(res)