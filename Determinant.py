# Calculate Determinant of a Matrix using Cofactor Expansion
def determinant(matrix):
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    elif len(matrix) == 1:
        return matrix[0]

    result = 0
    for index, num in enumerate(matrix[0]):
        newMatrix = []
        minor = num if index % 2 == 0 else -num
        for indexColumn, column in enumerate(matrix):
            if indexColumn == 0:
                continue

            rowMatrix = []
            for indexRow, value in enumerate(column):
                if indexRow != index:
                    rowMatrix.append(value)

            newMatrix.append(rowMatrix)

        result += (minor * determinant(newMatrix))

    return result
