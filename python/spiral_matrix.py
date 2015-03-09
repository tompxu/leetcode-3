class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        result = []
        m = len(matrix)
        if m == 0:
            return []
        n = len(matrix[0])
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        k = 0
        (x, y) = movement[k]
        while True:
            if i >= m or j >= n or matrix[i][j] == "*":
                i = i - x
                j = j - y
                k = (k + 1) % 4
                (x, y) = movement[k]
                i = i + x
                j = j + y
            if i >= m or j >= n or matrix[i][j] == "*":
                break
            else:
                result.append(matrix[i][j])
                matrix[i][j] = "*"
            i = i + x
            j = j + y
        return result