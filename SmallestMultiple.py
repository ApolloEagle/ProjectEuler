def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b//gcd(a, b)

def smallestMultiple(n):

    for i in range(1, n + 1):
        n = lcm(n, i)

    return n

print(smallestMultiple(20))