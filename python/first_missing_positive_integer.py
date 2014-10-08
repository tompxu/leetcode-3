class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        temp = [0 for i in range(len(A)+1)]
        for item in A:
            if item < len(temp) and item > 0:
                temp[item] += 1
        i = 1
        while i < len(temp):
            if temp[i] == 0:
                return i
            else:
                i += 1
        return i