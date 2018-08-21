def sumSquareDifference(n):

    squareOfSums = []
    sumOfSquares = []
    for i in range(1, n + 1):
        squareOfSums.append(i)
    x = (sum(squareOfSums))**2

    for j in range(1, n + 1):
        sumOfSquares.append(j**2)
    y = sum(sumOfSquares)

    return (x - y)

print(sumSquareDifference(100))

#Testing SSH