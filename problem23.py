import arithm


def abundants(max: int):
    res = []
    for i in range(max + 1):
        if sum(arithm.factors(i)) > i:
            res.append(i)
    return res

if __name__ == '__main__':
    l = abundants(28123)
    r = set()
    for i in l:
        for j in l:
            r.add(i+j)
    print(sum(filter(lambda n: n not in r, range(28123))))