import Determinant
import Invers

# Run this Program to Start

size = int(input('How much is the size (size > 0)? '))
matrix = []

for i in range(0, size):
    row = []
    for j in range(0, size):
        row.append(int(input('(' + str(i) + ', ' + str(j) + ') ')))

    matrix.append(row)

print('Determinant : ' + str(Determinant.determinant(matrix)))
print('Matrix : ')
for row in matrix:
    print(row)
print('Inverse : ')

inverse = Invers.inverse(matrix)
if len(inverse) == 0:
    print('Not Invertible')
else:
    for row in Invers.inverse(matrix):
        print(row)
