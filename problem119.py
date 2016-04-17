
def sum_digits(n):
    return sum(int(k) for k in str(n))

def solve119(n=30):
    powerdi = []
    for k in range(1000):
        for l in range(100):
            if sum_digits(k**l) == k:
                powerdi.append(k**l)
    powerdi.sort()
    return powerdi