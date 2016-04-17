if __name__ == '__main__':
    dpal = []
    for k in range(1000000):
        d = [int(c) for c in list(str(k))]
        if d[-1::-1] == d:
            db = [int(c) for c in list(bin(k))[2:]]
            if db[-1::-1] == db:
                print(k)
                dpal.append(k)
    print(dpal)
    