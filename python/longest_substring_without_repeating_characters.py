class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        if len(s) <= 1:
            return len(s)
        else:
            i = 1
            k = 0
            l = 1
            while k < len(s) - l and i < len(s):
                for j in xrange(k,i+1):
                    if i == j:
                        if l < j - k + 1:
                            l = j - k + 1
                    else:
                        if s[j] == s[i]:
                            k = j + 1
                            break
                i += 1
            return l