class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        l = len(s)
        total = 0
        for i in range(l):
            total = total * 26 + ord(s[i]) - ord('A') + 1
        return total