from itertools import combinations
from copy import copy


def triang(n):
    return (n * (n + 1))//2

def num_div(n):
    fact = factorize(n)
    res = 1
    for val in fact.values():
        res *= val + 1
    return res


if __name__ == '__main__':
    res = 1
    while True:
        if num_div(triang(res)) > 500:
            print(res)
            break
        res += 1
    print('fin')