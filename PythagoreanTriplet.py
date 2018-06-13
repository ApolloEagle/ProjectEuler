n = 1000

for a in range(1, n + 1):
    for b in range(a, n + 1):
        c = n - a - b
        if a**2 + b**2 == c**2:
            print(a * b * c)