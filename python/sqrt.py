class Solution:
    # @param x, an integer
    # @return an integer
    def sqrt(self, x):
        def estimate(y, guess):
            if abs(guess * guess - y) < 0.01:
                return guess
            else:
                return estimate(y, (y*1.0/guess+guess)/2.0)
        return int(estimate(x,x/2.0))