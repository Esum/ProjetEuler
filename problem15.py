def lattice(n: int):
    res = [ [ 1 for j in range(n) ] for i in range(n) ]
    for i in range(1, n):
        for j in range(1, n):
            res[i][j] = res[i-1][j] + res[i][j-1]
    return res

if __name__ == '__main__':
    print(lattice(21))
