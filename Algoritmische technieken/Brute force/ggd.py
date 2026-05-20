import random, time

def ggd(a,b):
    grootste_deler = -1
    kleinste = min(a,b)
    for deler in range(2,kleinste+1):
        if a % deler == 0 and b % deler == 0:
            grootste_deler = deler
    return grootste_deler


for keer in range(10000):
    start = time.time()
    a = random.randint(1,1000000)
    b = random.randint(1,1000000)
    g = ggd(a,b)
    eind = time.time()
    print(f"GGD van {a} en {b} is {g} ({eind-start})")