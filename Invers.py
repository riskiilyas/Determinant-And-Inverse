import Determinant


# Calculate Inverse of a Matrix using Cofactor Expansion
def inverse(matrix):

    # Calculate the Determinant First
    determinant = Determinant.determinant(matrix)

    # End the Program if the determinant is 0, because it's not invertible
    if determinant == 0:
        return []

    # Just the value of the element if size is 1x1
    if len(matrix) == 1:
        return [1/matrix[0][0]] if matrix[0][0] != 0 else []

    # Return the Adjoin of 2x2 matrix and divide each element by the determinant
    elif len(matrix) == 2:
        inverseMatrix = [[matrix[1][1]/determinant, (matrix[0][1] * -1)/determinant],
                         [(matrix[1][0] * -1)/determinant, matrix[0][0]/determinant]]
        return inverseMatrix

    # Calculation if the matrix size is greater than 2x2

    # The matrix that will be modified to be Adjoin
    modifiedMatrix = []

    # Iterate each element
    for indexRow, row in enumerate(matrix):

        # Row that will be added to modifiedMatrix
        modifiedRow = []
        for indexColumn, element in enumerate(row):

            # Matrix to store minor of the element entry
            newMatrix = []

            # Iterate Each Row again to store to the newMatrix
            for iRow, nRow in enumerate(matrix):

                # Row that will be stored to newMatrix
                newRow = []

                # Iterate each element of the iRow-th row
                for iColumn, nElement in enumerate(nRow):

                    # Add the element to newRow if the row & Column index are not the same with the entry
                    if iRow != indexRow and iColumn != indexColumn:
                        newRow.append(nElement)

                # Don't Add the newRow to the newMatrix if it doesn't contain any element
                if len(newRow) != 0:
                    newMatrix.append(newRow)

            # The new value of the entry is the determinant of its minor
            newValue = Determinant.determinant(newMatrix) * int(pow(-1, indexRow + indexColumn))

            # Add the newValue to the modifiedRow
            modifiedRow.append(newValue)

        # Add the modifiedRow to the modifiedMatrix after all the elements of indexRow-th row added
        modifiedMatrix.append(modifiedRow)

    # Declare the Inverse Matrix
    inverseMatrix = []

    # Iteration to Transpose the modifiedMatrix to be Adjoin
    for i in range(0, len(modifiedMatrix)):

        # Row to Add to the Inverse Matrix
        InverseMatrixRow = []
        for j in range(0, len(modifiedMatrix)):

            # Position the element with Transpose Rule & Also divide by determinant to get the Inverse
            InverseMatrixRow.append(modifiedMatrix[j][i] / determinant)

        # Add the InverseMatrixRow to the InverseMatrix
        inverseMatrix.append(InverseMatrixRow)

    # Finish
    return inverseMatrix
