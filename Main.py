import Determinant
import Invers

for row in Invers.inverse([[1, 1, 0, 2], [0, 0, 3, 7], [1, 2, 4, 1], [0, 3, 0, 1]]):
    print(row)

for row in Invers.inverse([[2, 1], [1, 1]]):
    print(row)

print(Determinant.determinant([[1, 1, 0, 2], [0, 0, 3, 7], [1, 2, 4, 1], [0, 3, 0, 1]]))
