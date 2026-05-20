n = 0

def merge_sort(lijst):
    global n
    if len(lijst) <= 1:
        return lijst

    n += 3
    midden = len(lijst)//2
    links = merge_sort(lijst[:midden])
    rechts = merge_sort(lijst[midden:])

    return merge(links,rechts)

def merge(linker,rechter):
    global n
    gesorteerd = []

    while len(linker) > 0 and len(rechter) > 0:
        eerste_linker = linker[0]
        eerste_rechter = rechter[0]

        if eerste_linker <= eerste_rechter:
            gesorteerd.append(linker.pop(0))
        else:
            gesorteerd.append(rechter.pop(0))

        n += 2
    
    gesorteerd.extend(linker)
    gesorteerd.extend(rechter)
    n += 2

    return gesorteerd

    
for i in range(4):
    n = 0
    merge_sort(list(range(1,1+(10**i))))
    print(n)
    n = 0
    merge_sort(list(range((10**i),0,-1)))
    print(n)
input()
lijsten = [
    [3],
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]

for i in range(len(lijsten)):
    lijsten[i] = merge_sort(lijsten[i])
    print(lijsten[i])