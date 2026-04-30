rows = 5
columns = 6

# 2 dimensionale array
doolhof = [[' ']*rows for kolom in range(columns)]

def toonDoolhof():
    for i in range(len(doolhof)):
        uitvoer = ""
        for j in range(len(doolhof[i])):
            uitvoer += f" |{doolhof[i][j]}| "
        print(uitvoer)

# A = startpunt, X = muur
doolhof[0][0] = "A"
doolhof[0][1] = "X"
doolhof[1][1] = "X"
doolhof[2][1] = "X"
doolhof[3][1] = "X"
doolhof[3][2] = "X"
doolhof[1][3] = "X"
doolhof[1][4] = "X"
doolhof[3][4] = "X"
# B = eindpunt
doolhof[columns-1][rows-1] = "B"

#toonDoolhof()

visited = []
def DFS(positie):
    x = positie[0]
    y = positie[1]

    # buiten doolhof
    if x < 0 or y < 0 or y >= rows or x >= columns:
         return False
    # inhoud van de cel
    inhoud = doolhof[x,y]
    # muur
    if inhoud == "X":
         return False
    if (x,y) in visited:
         return False
    # huidige cel toevoegen aan bezochte cellen
    visited.append((x,y))
    if inhoud == "B":
         return True
    erboven = (x,y-1)
    rechts = (x+1,y)
    eronder = (x,y+1)
    links = (x-1,y)
    richtingen = [erboven, rechts, eronder, links]
    for richting in richtingen:
        stap = DFS(richting)
        if stap == True:
             return True
    

start = None 
for i in range(len(doolhof)):
        for j in range(len(doolhof[i])):
            if doolhof[i][j] == "A":
                start = (i,j)

route = DFS(start)
print(route)
toonDoolhof()
