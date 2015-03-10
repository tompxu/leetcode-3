class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        s = 0
        if n <= 0:
            return 0
        else:
            while n >=5:
                s += n / 5
                n = n / 5
        return s