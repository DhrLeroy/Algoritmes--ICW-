def faculteit(n):
    print(f"Begin berekenen faculteit {n}")
    if n == 1:
        return 1
    uitkomst = n * faculteit(n-1)
    print(f"Gedaan met berekenen faculteit {n}")
    return uitkomst

getal = int(input("Getal: "))
print(f'Faculteit {getal} = {faculteit(getal)}')


