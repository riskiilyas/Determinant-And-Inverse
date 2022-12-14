# Calculate Determinant of a Matrix using Cofactor Expansion
def determinant(matrix):
    # Do the Sar-rus method if matrix is 2x2
    if len(matrix) == 2:
        return (matrix[0][0] * matrix[1][1]) - (matrix[1][0] * matrix[0][1])
    # Return the element if matrix 1x1
    elif len(matrix) == 1:
        return matrix[0][0]

    # Calculation if matrix is greater than 2x2

    # Make result variable to calculate total of the minor matrices determinant
    result = 0

    # Cofactor Expansion using First Row
    for index, num in enumerate(matrix[0]):
        # Matrix to store the Minor of a(index) entry
        minorMatrix = []

        # The entry value (negative if the position is even)
        entry = num if index % 2 == 0 else -num

        # Iterate the Row
        for indexRow, row in enumerate(matrix):

            # Skip if the column is the first (that's the cofactor's entry row)
            if indexRow == 0:
                continue

            # Matrix to store the Minor Row
            rowMinor = []

            # Iterate the columns of the indexRow-th row
            for indexColumn, value in enumerate(row):

                # Add the element if the Column index is not the same with the entry's
                if indexColumn != index:
                    rowMinor.append(value)

            # Add the row to the matrix
            minorMatrix.append(rowMinor)

        # Add the result and call the determinant function recursively until the size is 2x2
        result += (entry * determinant(minorMatrix))

    # The result is the sum of all determinants of the minors
    return result
