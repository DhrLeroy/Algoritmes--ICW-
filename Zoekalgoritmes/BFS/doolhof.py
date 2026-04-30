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

def BFS():
    # lijst te over lopen plaatsen
    open_plaatsen = []
    visited = []

    # beginpunt zoeken
    for i in range(len(doolhof)):
        for j in range(len(doolhof[i])):
            if doolhof[i][j] == "A":
                x = (i,j)
                open_plaatsen.append((i,j))

    while len(open_plaatsen) > 0:
        # bovenste (0) element van de lijst halen
        huidige = open_plaatsen.pop(0)
        x = huidige[0]
        y = huidige[1]

        # controleren of cel wel in doolhof vindt  
        if x < 0 or y < 0 or y >= rows or x >= columns:
            continue
        # OF je hebt deze cel reeds bezocht (visited)
        if (x,y) in visited:
            continue
        # OF deze cel is een muur (X)
        if doolhof[x][y] == "X":
            continue
        # continue = naar volgende iteratie gaan

        # als je B hebt gevonden, geef je de lijst van bezochte cellen door (pad)
        if doolhof[x][y] == "B":
            return visited
        else:
            # huidige cel toevoegen aan de bezochte plaatsen
            visited.append((x,y))

        # cellen bepalen die rond deze cel liggen en toevoegen achteraan de lijst van te overlopen plaatsen
        erboven = (x,y-1)
        rechts = (x+1,y)
        eronder = (x,y+1)
        links = (x-1,y)
        open_plaatsen.append(erboven)
        open_plaatsen.append(rechts)
        open_plaatsen.append(eronder)
        open_plaatsen.append(links)

route = BFS()
print(route)
toonDoolhof()
