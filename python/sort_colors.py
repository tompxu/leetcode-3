class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        i = 0
        for l in range(len(A)):
            if A[i] == 0:
                m = A.pop(i)
                A.insert(0,m)
                i += 1
            elif A[i] == 2:
                m = A.pop(i)
                A.append(m)    
            else:
                i += 1
        return A