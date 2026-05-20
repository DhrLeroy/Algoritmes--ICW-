import random

def zoeken(lst,gezocht):
    dichtste = 1000000000
    for j in range(len(lst)):
        if abs(lst[j]-gezocht) < dichtste:
            dichtste = lst[j]
    return dichtste

for keer in range(10):
    lst = []
    for i in range(100):
        lst.append(random.randint(1,100000))
    lst.sort()
    gezocht = random.randint(1,100000)
    teller = 0
    positie = 0

    d = zoeken(lst,gezocht)

    print(f'De dichtste waarde bij {gezocht} was {d}')

    
            

    
