import Determinant


# Calculare Inverse of a Matrix using Cofactor Expansion
def inverse(matrix):
    determinant = Determinant.determinant(matrix)
    if determinant == 0:
        return None

    if len(matrix) == 1:
        return [1/matrix[0]]
    elif len(matrix) == 2:
        result = [[matrix[1][1]/determinant, (matrix[0][1] * -1)/determinant],
                  [(matrix[1][0] * -1)/determinant, matrix[0][0]/determinant]]
        return result

    modifiedMatrix = []
    for indexColumn, column in enumerate(matrix):
        modifiedRow = []
        for indexRow, num in enumerate(column):

            newMatrix = []
            for iColumn, nColumn in enumerate(matrix):
                newRow = []
                for iRow, nRow in enumerate(nColumn):
                    if iColumn != indexColumn and iRow != indexRow:
                        newRow.append(nRow)

                if len(newRow) != 0:
                    newMatrix.append(newRow)

            newValue = Determinant.determinant(newMatrix) * int(pow(-1, indexColumn + indexRow))

            modifiedRow.append(newValue)

        modifiedMatrix.append(modifiedRow)

    result = []
    for i in range(0, len(modifiedMatrix)):
        adjointRow = []
        for j in range(0, len(modifiedMatrix)):
            adjointRow.append(modifiedMatrix[j][i] / determinant)

        result.append(adjointRow)

    return result
