def fibonacci(n:int):
    a = 1
    b = 1
    for i in range(n-2):
        a, b = a+b, a
    return a



if __name__ == '__main__':
    n = 0
    while len(str(fibonacci(n))) < 1000:
        n += 1
    print(n)