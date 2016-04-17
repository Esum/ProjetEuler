
def I(x, calls=100):
    if calls == 0:
        return 0
    if x >= 1:
        return 1/2 + I(x-1, calls-1)
    elif 1/2 < x < 2:
        return 1/2 - I(1-x, calls-1)
    elif 0 <= x <= 1/2:
        return I(2*x, calls-1)/4 + x*x/2
    else:
        return -I(-x)
