def insertion_sort(lijst):
    print(lijst)
    for stap in range(1,len(lijst)):
        waarde = lijst[stap]
        index_vorige_waarde = stap - 1
        while index_vorige_waarde >= 0 and lijst[index_vorige_waarde] > waarde:
            lijst[index_vorige_waarde+1] = lijst[index_vorige_waarde]
            print(f"  {lijst}")
            index_vorige_waarde = index_vorige_waarde-1
        lijst[index_vorige_waarde+1] = waarde
        print(f" {lijst}")


lijsten = [
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]

for lijst in lijsten:
    insertion_sort(lijst)
    input()
    print(lijst)