import random

def quicksort(lijst):

    if len(lijst) <= 1:
        return lijst

    # middelste waarde in plaats van mediaan
    middelste = lijst[len(lijst)//2]

    kleiner = []
    groter = []
    gelijk = []

    for getal in lijst:
        if getal < middelste:
            kleiner.append(getal)
        elif getal > middelste:
            groter.append(getal)
        else:
            gelijk.append(getal)
    
    # kleinere lijst sorteren
    kleiner = quicksort(kleiner)
    # grotere lijst sorteren
    groter = quicksort(groter)

    # kleinere (gesorteerde) lijst uitbreiden met de waarden die gelijk waren aan de middelste waarde
    kleiner.extend(gelijk)
    # kleinere (en gelijke) lijst nog eens uitbreiden met de (gesorteerde) waarden die groter waren dan de middelste waarde
    kleiner.extend(groter)

    return kleiner


lijsten = [
    [3],
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]


for i in range(len(lijsten)):
    lijsten[i] = quicksort(lijsten[i])
    print(lijsten[i])


randomlijst = []
for i in range(100):
    randomlijst.append(random.randint(-100,100))
print(randomlijst)
print(quicksort(randomlijst))