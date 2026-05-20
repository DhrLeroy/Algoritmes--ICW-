def binair_zoeken(lijst,zoekwaarde,extra):

    if len(lijst) == 0:
        return -1

    midden = len(lijst)//2
    middenste_getal = lijst[midden]

    if middenste_getal == zoekwaarde:
        return midden + extra
    elif middenste_getal < zoekwaarde:
        extra = extra + midden+1
        return binair_zoeken(lijst[midden+1:], zoekwaarde, extra)
    else:
        return binair_zoeken(lijst[:midden], zoekwaarde, extra)



lijst = [-3, 1, 8, 64, 76, 77, 128, 906]

zoekwaardes = [23, 1, 64, 77, 906]

for zoekwaarde in zoekwaardes:
    print(f'{zoekwaarde} staat op de {binair_zoeken(lijst, zoekwaarde,0)}de plaats')