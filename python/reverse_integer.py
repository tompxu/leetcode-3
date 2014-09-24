class Solution:
    # @return an integer
    def reverse(self, x):
        n = 1
        if x < 0:
            n = -1
        x = x / n
        temp = 0
        while x > 0:
            temp = temp * 10 + x % 10
            x /= 10
        return n * temp