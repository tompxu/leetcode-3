class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        i = 0
        j = len(A) - 1
        while i <= j:
            k = ( i + j )/2
            if A[k] == target:
                return k
            elif A[k] > target:
                j = k - 1
            else:
                i = k + 1
        return i