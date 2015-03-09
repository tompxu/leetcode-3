class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        numbers = [i + 1 for i in range(n**2)]
        numbers = list(reversed(numbers))
        matrix = [[0 for i in range(n)] for j in range(n)]
        movement = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        i, j = 0, 0
        k = 0
        (x, y) = movement[k]
        if n <= 0:
            return []
        if n == 1:
            return [[1]]
        while True:
            if i >= n or j >= n or matrix[i][j]  != 0:
                i = i - x
                j = j - y
                k = (k + 1) % 4
                (x, y) = movement[k]
                i = i + x
                j = j + y
                if i >= n or j >= n:
                    break
            if len(numbers) == 0:
                break
            else:
                matrix[i][j] = numbers.pop()
            i = i + x
            j = j + y
        return matrix 
        