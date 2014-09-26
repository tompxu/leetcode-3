class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        output = [[] for i in range(numRows)]
        for i in range(numRows):
            for j in range(i+1):
                if (j == 0) or (j == i):
                    output[i].append(1)
                else:
                    output[i].append(output[i-1][j-1] + output[i-1][j])
        return output