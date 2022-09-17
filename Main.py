import Determinant
import Invers

# Run this Program to Start

size = int(input('How much is the size (size > 0)? '))
matrix = []

print('Input the Row Separate with Space (\' \')')
for i in range(0, size):
    row = []
    rowInput = input('Row ' + str(i+1) + ' : ').split(' ')
    for j in range(0, size):
        row.append(int(rowInput[j]))

    matrix.append(row)

print('Determinant : ' + str(Determinant.determinant(matrix)))
print('Inverse : ')

inverse = Invers.inverse(matrix)
if len(inverse) == 0:
    print('Not Invertible')
else:
    for row in Invers.inverse(matrix):
        print(row)
