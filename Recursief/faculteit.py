def faculteit(n):
    if n == 0:
        return 1
    return n * faculteit(n-1)

getal = int(input("Getal: "))
print(f'Faculteit {getal} = {faculteit(getal)}')


