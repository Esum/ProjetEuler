__author__ = 'Benjamin'


if __name__ == '__main__':
    res = 0
    for i in range(2, 1000000):
        if i == sum([int(d)**5 for d in list(str(i))]):
            res += i
    print(res)