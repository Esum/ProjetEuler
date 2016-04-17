def totients(n):
    phi = [0]*n
    phi[1] = 1
    for i in range(2, n):
        if phi[i] == 0:
            phi[i] = i - 1
            j = 2
            while j * i < n:
                if phi[j] != 0:
                    q = j
                    f = i - 1
                    while q % i == 0:
                        f *= i
                        q //= i
                    phi[i * j] = f * phi[q]
                j += 1
        i += 1
    return phi