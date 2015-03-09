class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        def isValid(board, i, j):
            for k in range(9):
                if  k != i and board[k][j] == board[i][j]:
                    return False
                if k != j and board[i][k] == board[i][j]:
                    return False
            for k1 in xrange(i/3 * 3, i/3*3+3):
                for k2 in xrange(j/3*3, j/3*3+3):
                    if k1 != i and k2 !=j and board[k1][k2] == board[i][j]:
                        return False
            return True
        
        def replace(s, j, k):
            s = list(s)
            s[j] = k
            return "".join(s)

        def solver(board):
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for k in xrange(1,10):
                            board[i] = replace(board[i], j, str(k))
                            if isValid(board, i, j) and solver(board):
                                return True
                            board[i] = replace(board[i], j, '.')
                        return False
            return True
        solver(board)
    
