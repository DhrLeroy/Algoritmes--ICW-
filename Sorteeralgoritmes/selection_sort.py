def selection_sort(lijst):
    for stap in range(len(lijst)):
        index_voorlopig_kleinste_waarde = stap

        for positie in range(index_voorlopig_kleinste_waarde+1,len(lijst)):
            if lijst[index_voorlopig_kleinste_waarde] > lijst[positie]:
                index_voorlopig_kleinste_waarde = positie
        
        if index_voorlopig_kleinste_waarde != stap:
            old_value = lijst[index_voorlopig_kleinste_waarde]
            lijst[index_voorlopig_kleinste_waarde] = lijst[stap]
            lijst[stap] = old_value

lijsten = [
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]

for lijst in lijsten:
    selection_sort(lijst)
    print(lijst)