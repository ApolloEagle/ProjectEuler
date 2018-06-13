n = 2000000
prime = []

for p in range(2, n + 1):
    for i in range(2, int(p ** 0.5) + 1):
        if p % i == 0:
            break
    else:
        prime.append(p)

print(sum(prime))