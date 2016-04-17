__author__ = 'Benjamin'


def permutations(E: list):
    if len(E) == 1:
        return [E]
    perms = permutations(E[:-1])
    res = []
    newelement = E[-1]
    for p in perms:
        for i in range(len(E)):
            res.append(p[:i] + [newelement] + p[i:])
    return res

if __name__ == '__main__':
    print(permutations([0,1,2,3,4,5,6,7,8,9])[-1000000])