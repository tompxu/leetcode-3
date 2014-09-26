class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0: return [1]
        output = []
        for i in range(rowIndex+1):
            temp = []
            for j in xrange(1,i):
                temp.append(output[j-1] + output[j])
            output = [1] + temp + [1]
        return output