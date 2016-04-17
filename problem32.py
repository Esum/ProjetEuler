if __name__ == '__main__':
    pand = []
    for i1 in range(1, 10):
        for i2 in range(1, 10):
            if i2 == i1:
                continue
            for i3 in range(1, 10):
                if i3 == i2 or i3 == i1:
                    continue
                for i4 in range(1, 10):
                    if i4 == i3 or i4 == i2 or i4 == i1:
                        continue
                    n = i4*1000 + i3*100 + i2*10 + i1
                    print(n)
                    for k in factors(n):
                        if len(str(k)) + len(str(n//k)) == 5:
                            d = list(str(k) + str(n//k) + str(n))
                            d.sort()
                            if d == [str(k) for k in range(1, 10)]:
                                print(k, n//k, n)
                                pand.append(n)
                                break
    print(pand)