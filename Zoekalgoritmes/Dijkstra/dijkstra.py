def dijkstra(graaf,begin,eind):
    visited = []
    unvisited = []

    resultaat = {}
    for key in graaf:
        unvisited.append(key)
        if key == begin:
            resultaat[key]=('',0)
        else:
            resultaat[key] = ("",float('inf'))



    current_node = begin

    while(True):
        current_distance = resultaat[current_node][1]
        for path in graaf[current_node]:
            punt = path[0]
            afstand = path[1]
            new_distance = current_distance + afstand
            if new_distance < resultaat[punt][1]:
                resultaat[punt] = (current_node,new_distance)
        unvisited.remove(current_node)
        visited.append(current_node)
        if len(unvisited) == 0 or current_node == float('inf'):
            break

        shortest_distance = float('inf')
        for punt in unvisited:
            distance_to_punt = resultaat[punt][1]
            if distance_to_punt <= shortest_distance:
                current_node = punt
                shortest_distance = distance_to_punt

    knooppunten = []

    previous_node = resultaat[eind][0]
    

    while previous_node != begin:
        knooppunten.insert(0,previous_node)
        previous_node = resultaat[previous_node][0]


    print(knooppunten)

    return resultaat


graaf = {
    "A": [("D",1),("B",6)],
    "B": [("A",6),("D",2),("C",5)],
    "C": [("B",5),("E",5)],
    "D": [("A",1),("B",2),("E",1)],
    "E":[("D",1),("B",2),("C",5)]
}

resultaat = dijkstra(graaf,"A", "B")

print(resultaat)
