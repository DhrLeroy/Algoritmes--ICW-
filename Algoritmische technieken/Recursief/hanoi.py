def hanoi(n, van, hulp, naar):
    if n == 1:
        print(f"Verplaats schijf {n} van {van} naar {naar}")
        return

    hanoi(n-1, van, naar, hulp)

    print(f"Verplaats schijf {n} van {van} naar {naar}")

    hanoi(n-1, hulp, van, naar)

hanoi(5,"A","B","C")