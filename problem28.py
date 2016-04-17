

if __name__ == '__main__':
    summ = 1
    k = 1
    ring = 0
    while k*k <= 999*999:
        k += 2
        ring += 2
        summ += 4 * k*k - 6 * ring
    