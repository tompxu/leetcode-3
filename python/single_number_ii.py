class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        temp = {}
        for i in A:
            t = str(i)
            if t not in temp:
                temp[t] = 1
            else:
                temp[t] += 1
        for i in temp:
            if temp[i] == 1:
                return int(i)