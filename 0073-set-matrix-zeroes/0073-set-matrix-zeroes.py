class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])

        # Step 1: Check if first row or column should be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))

        # Step 2: Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Step 3: Apply zeroing based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # Step 4: Zero first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0

        # Step 5: Zero first column if needed
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
