def primes(n):
    primes = [2]
    counter = 3
    while len(primes) < n:
        if all(counter % prime != 0 for prime in primes):
            primes.append(counter)
        counter += 2
    return primes[-1]

print(primes(10001))