def largestPrimeFactor(n):

    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n

print(largestPrimeFactor(600851475143))