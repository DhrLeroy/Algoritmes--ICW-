def bubble_sort(lijst):
    for aantal in range(len(lijst),0,-1):
        for positie in range(aantal-1):
            if lijst[positie] > lijst[positie+1]:
                old_value = lijst[positie+1]
                lijst[positie + 1] = lijst[positie]
                lijst[positie] = old_value
    
for i in range(8):
    bubble_sort(list(range(1,1+(10**i))))
    bubble_sort(list(range((10**i),0,-1)))

lijsten = []
for lijst in lijsten:
    bubble_sort(lijst)
    #print(lijst)