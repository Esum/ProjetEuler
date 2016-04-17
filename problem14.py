import sys
sys.setrecursionlimit(1000000)


def syracuse(n: int, res=[]):
    if n == 1:
        return res + [1]
    elif n%2:
        return syracuse(3*n + 1, res + [n])
    else:
        return syracuse(n//2, res + [n])


if __name__ == '__main__':
    res = 0
    for i in range(800000, 9000000):
        if len(syracuse(i)) > res:
            res = len(syracuse(i))
            print(i, res)
    print(res)