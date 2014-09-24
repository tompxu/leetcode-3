class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        N = len(matrix)
        for i in range(N):
            for j in range(i, N-i-1):
                temp = matrix[i][j]
                matrix[i][j] =  matrix[N-1-j][i]
                matrix[N-1-j][i] = matrix[N-1-i][N-1-j]
                matrix[N-1-i][N-1-j] = matrix[j][N-1-i]
                matrix[j][N-1-i] = temp
        return matrix