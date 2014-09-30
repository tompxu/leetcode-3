class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i = 0
        while i < len(A) - 1:
            if A[i] != A[i+1]:
                i += 1
            elif i == len(A) - 2:
                break
            elif A[i] == A[i+2]:
                del A[i]
            else:
                i += 2
        return len(A)