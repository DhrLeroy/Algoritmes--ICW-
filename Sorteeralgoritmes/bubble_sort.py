def bubble_sort(lijst):
    for aantal in range(len(lijst),0,-1):
        for positie in range(aantal-1):
            if lijst[positie] > lijst[positie+1]:
                old_value = lijst[positie+1]
                lijst[positie + 1] = lijst[positie]
                lijst[positie] = old_value

lijsten = [
    [5 , 2 , 4 , 1],
    [3 , 1 , 2 , 4],
    [5 , 2 , 4 , 1],
    [7 , 3 , 5 , 2 , 6],
    [1 , 3 , 2 , 4 , 5]
]

for lijst in lijsten:
    bubble_sort(lijst)
    print(lijst)