class Solution:
    # @param A, a list of integers
    # @return a boolean
    def canJump(self, A):
        l = 0
        for i in range(len(A)):
            if i <= l:
                if l < A[i] + i:
                    l = A[i] + i
                if l >= len(A) -1:
                    return True
        return False