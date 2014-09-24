class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        if x < 0:
            return False
        elif x < 10:
            return True
        else:
            n = 0
            t = x
            while t > 0:
                t /= 10
                n += 1
            temp = 1
            for i in range(n-1):
                temp *= 10
            while x > 0:
                if x / temp == x % 10:
                    x = (x - x / temp * temp) / 10
                    temp /= 100
                else:
                    return False
            return True