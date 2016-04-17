from random import randint, shuffle
from copy import copy

class case:
    GO = 0
    A1 = 1
    CC1 = 2
    A2 = 3
    T1 = 4
    R1 = 5
    B1 = 6
    CH1 = 7
    B2 = 8
    B3 = 9
    JAIL = 10
    C1 = 11
    U1 = 12
    C2 = 13
    C3 = 14
    R2 = 15
    D1 = 16
    CC2 = 17
    D2 = 18
    D3 = 19
    FP = 20
    E1 = 21
    CH2 = 22
    E2 = 23
    E3 = 24
    R3 = 25
    F1 = 26
    F2 = 27
    U2 = 28
    F3 = 29
    G2J = 30
    G1 = 31
    G2 = 32
    CC3 = 33
    G3 = 34
    R4 = 35
    CH3 = 36
    H1 = 37
    T2 = 38
    H2 = 39

class goto:
    nextR = 40
    nextU = 41
    prev3 = 42

CC = [None]*14 + [case.GO, case.JAIL]
CH = [None]*6 + [case.GO, case.JAIL, case.C1, case.E3, case.H2, case.R1, goto.nextR, goto.nextR, goto.nextU, goto.prev3]


def jouer(coups=100, dices=6, CC=[None]*14 + [case.GO, case.JAIL], CH=[None]*6 + [case.GO, case.JAIL, case.C1, case.E3, case.H2, case.R1, goto.nextR, goto.nextR, goto.nextU, goto.prev3]):
    cc = copy(CC)
    ch = copy(CH)
    shuffle(cc)
    shuffle(ch)
    stats = {k: 0 for k in range(40)}
    coup = 0
    case_joueur = case.GO
    stats[case.GO] = 1
    while coup < coups:
        replays = True
        doubles = 0
        while replays:
            replays = False
            d1 = randint(1, dices)
            d2 = randint(1, dices)
            if d1 == d2:
                if doubles == 2:
                    case_joueur = case.JAIL
                    doubles = 0
                    replays = False
                    break
                else:
                    replays = True
                    doubles += 1
            else:
                doubles = 0
            case_joueur = (case_joueur + d1 + d2) % 40
            if case_joueur in [case.CH1, case.CH2, case.CH3]:
                carte_piochee = ch.pop()
                ch = [carte_piochee] + ch
                if carte_piochee is not None:
                    if carte_piochee == goto.nextR:
                        if case.R4 < case_joueur or case_joueur < case.R1:
                            case_joueur = case.R1
                        elif case_joueur < case.R2:
                            case_joueur = case.R2
                        elif case_joueur < case.R3:
                            case_joueur = case.R3
                        elif case_joueur < case.R4:
                            case_joueur = case.R4
                    elif carte_piochee == goto.nextU:
                        if case.U2 < case_joueur or case_joueur < case.U1:
                            case_joueur = case.U1
                        else:
                            case_joueur = case.U2
                    elif carte_piochee == goto.prev3:
                        case_joueur = (case_joueur - 3) % 40
                    else:
                        case_joueur = carte_piochee
                        if case_joueur == case.JAIL:
                            replays = False
            if case_joueur in [case.CC1, case.CC2, case.CC3]:
                carte_piochee = cc.pop()
                cc = [carte_piochee] + cc
                if carte_piochee is not None:
                    case_joueur = carte_piochee
                    if case_joueur == case.JAIL:
                        replays = False
            if case_joueur == case.G2J:
                case_joueur = case.JAIL
                replays = False
        stats[case_joueur] += 1
        coup += 1
    return {k: stats[k]/(coups+1) for k in stats}