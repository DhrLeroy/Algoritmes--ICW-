import random

def zoeken(lst,gezocht):
    for j in range(len(lst)):
        if lst[j] == gezocht:
            return j
    return -1

for keer in range(10):
    lst = []
    for i in range(100):
        lst.append(random.randint(1,100))
    gezocht = random.randint(1,100)
    teller = 0
    positie = 0

    print(zoeken(lst,gezocht))

    
            

    
