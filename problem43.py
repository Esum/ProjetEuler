def solve43():
    res = set()
    for d1 in range(10):
        for d2 in range(10):
            if d2 == d1:
                continue
            for d3 in range(10):
                if d3 == d2 or d3 == d1:
                    continue
                for d4 in range(10):
                    if d4 == d3 or d4 == d2 or d4 == d1:
                        continue
                    for d5 in range(10):
                        if d5 == d4 or d5 == d3 or d5 == d2 or d5 == d1:
                            continue
                        for d6 in range(10):
                            if d6 == d5 or d6 == d4 or d6 == d3 or d6 == d2 or d6 == d1:
                                continue
                            for d7 in range(10):
                                if d7 == d6 or d7 == d5 or d7 == d4 or d7 == d3 or d7 == d2 or d7 == d1:
                                    continue
                                for d8 in range(10):
                                    if d8 == d7 or d8 == d6 or d8 == d5 or d8 == d4 or d8 == d3 or d8 == d2 or d8 == d1:
                                        continue
                                    for d9 in range(10):
                                        if d9 == d8 or d9 == d7 or d9 == d6 or d9 == d5 or d9 == d4 or d9 == d3 or d9 == d2 or d9 == d1:
                                            continue
                                        for d10 in range(10):
                                            if d10 == d9 or d10 == d8 or d10 == d7 or d10 == d6 or d10 == d5 or d10 == d4 or d10 == d3 or d10 == d2 or d10 == d1:
                                                continue
                                            if (100*d2 + 10*d3 + d4) % 2 == 0:
                                                if (100*d3 + 10*d4 + d5) % 3 == 0:
                                                    if (100*d4 + 10*d5 + d6) % 5 == 0:
                                                        if (100*d5 + 10*d6 + d7) % 7 == 0:
                                                            if (100*d6 + 10*d7 + d8) % 11 == 0:
                                                                if (100*d7 + 10*d8 + d9) % 13 == 0:
                                                                    if (100*d8 + 10*d9 + d10) % 17 == 0:
                                                                        res.add(int(str(d1)+str(d2)+str(d3)+str(d4)+str(d5)+str(d6)+str(d7)+str(d8)+str(d9)+str(d10)))
    return sum(res)
                                                
                                                
                                                