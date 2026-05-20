coefficienten = [6,-7,-9,-2]

constante = coefficienten[len(coefficienten)-1]

delers = []

for mogelijkeDeler in range(1,abs(constante)+1):
    if constante % mogelijkeDeler == 0:
        delers.append(mogelijkeDeler)
        delers.append(-mogelijkeDeler)

nulwaarde = 0
for deler in delers:
    functiewaarde = 0
    # start = 4 -1  einde = -1 (excl.)   stap = -1 want iedere keer -1
    teller = 0
    for exponent in range(len(coefficienten)-1,-1,-1):
        functiewaarde = functiewaarde + (coefficienten[teller]*(deler**exponent))
        positie = len(coefficienten)-1 - exponent
        functiewaarde = functiewaarde + (coefficienten[positie]*(deler**exponent))
        teller = teller + 1
    
    if round(functiewaarde,10) == 0:
        nulwaarde = deler

