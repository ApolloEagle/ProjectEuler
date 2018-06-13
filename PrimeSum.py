def primeSum(n):
    prime = []

    for p in range(2, n + 1):
        for i in range(2, int(p ** 0.5) + 1):
            if p % i == 0:
                break
        else:
            prime.append(p)
    return sum(prime)

print(primeSum(2000000))