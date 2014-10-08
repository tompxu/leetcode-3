class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        def isValid(string):
            temp = ""
            for i in string:
                if i.isdigit():
                    temp += i
            return len(set(temp)) == len(temp)
        for i in range(9):
            subarray = ""
            for j in range(9):
                subarray += board[j][i]
            if not isValid(board[i]) or not isValid(subarray):
                return False
        for i in range(3):
            for j in range(3):
                subarray = board[i*3][j*3:j*3+3] + board[i*3+1][j*3:j*3+3] + board[i*3+2][j*3:j*3+3]
                if not isValid(subarray):
                    return False
        return True