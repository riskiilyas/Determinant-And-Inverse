import Determinant
import Invers

size = int(input('How much is the size? '))
matrix = []

for i in range(0, size):
    row = []
    for j in range(0, size):
        row.append(int(input('(' + str(i) + ', ' + str(j) + ') ')))

    matrix.append(row)

print('Determinant: ' + str(Determinant.determinant(matrix)))
print('Invers: ')
for row in Invers.inverse(matrix):
    print(row)

