class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        i = 0
        for j in range(n):
            while i < m:
                if A[i] < B[j]:
                    i += 1
                else:
                    break
            A.insert(i,B[j])
            m += 1