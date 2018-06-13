squareOfSums = []
sumOfSquares = []
for i in range(1, 101):
    squareOfSums.append(i)
x = (sum(squareOfSums))**2

for j in range(1, 101):
    sumOfSquares.append(j**2)
y = sum(sumOfSquares)

print(x - y)