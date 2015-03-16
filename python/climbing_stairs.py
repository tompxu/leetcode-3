class Solution:
    # @param n, an integer
    # @return an integer
    def climbStairs(self, n):
        num = [0 for i in range(n+1)]
        for i in range(n+1):
            if i == 0:
                num[i] = 0
            elif i == 1:
                num[i] = 1
            elif i == 2:
                num[i] = 2
            else:
                num[i] = num[i-1] + num[i-2]
        return num[-1]