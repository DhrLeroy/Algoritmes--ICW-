def merge_sort(lijst):
    if len(lijst) <= 1:
        return lijst

    midden = len(lijst)//2
    links = merge_sort(lijst[:midden])
    rechts = merge_sort(lijst[midden:])

    return merge(links,rechts)

def merge(linker,rechter):
    gesorteerd = []

    while len(linker) > 0 and len(rechter) > 0:
        eerste_linker = linker[0]
        eerste_rechter = rechter[0]

        

lijsten = [
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]

for lijst in lijsten:
    merge_sort(lijst)
    print(lijst)