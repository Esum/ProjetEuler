from itertools import chain

pieces = [1, 2, 5, 10, 20, 50, 100, 200]

def facons(n):
    res = {k: [] for k in range(1, n+1)}
    for k in range(1, n+1):
        if k in pieces:
            res[k].append({k: 1})
        for i in pieces:
            if i >= k:
                break
            for facon_i in res[i]:
                for facon_kmi in res[k-i]:
                    facon = {}
                    for l in chain(facon_i.keys(), facon_kmi.keys()):
                        if l in facon_i.keys() and l in facon_kmi.keys():
                            facon[l] = facon_i[l] + facon_kmi[l]
                        elif l in facon_i.keys():
                            facon[l] = facon_i[l]
                        elif l in facon_kmi.keys():
                            facon[l] = facon_kmi[l]
                    if not (facon in res[k]):
                        res[k].append(facon)
    return res[n]
    