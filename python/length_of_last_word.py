class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        if s.split() == []:
            return 0
        else:
            return len(s.split()[-1])