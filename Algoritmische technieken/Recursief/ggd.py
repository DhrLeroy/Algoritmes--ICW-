import random
import time

def ggd(a,b):
    
    if b == 0:
        return a
    else:
        return ggd(b, a % b)



for keer in range(10000):
    start = time.time()
    a = random.randint(1,1000000)
    b = random.randint(1,1000000)
    g = ggd(a,b)
    eind = time.time()
    print(f"GGD van {a} en {b} is {g} ({eind-start})")
