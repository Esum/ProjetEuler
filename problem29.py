if __name__ == '__main__':
    res = set()
    for a in range(2, 101):
        for b in range(2, 101):
            res.add(a**b)
    print(len(res))