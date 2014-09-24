class Solution:
    # @return a string
    def longestPalindrome(self, s):
        x = 0
        y = 0
        z = 1
        l = s[0]
        if len(s) <= 1:
            return s
        while y < len(s) - len(l)/2 and z < len(s):
            if y > 0 and s[y-1] == s[z]:
                x = y - 1
                while x - 1 >= 0 and z + 1 < len(s):
                    if s[x-1] == s[z+1]:
                        x -=1
                        z += 1
                    else:
                        break
                if len(l) < z - x + 1:
                    l = s[x:z+1]
                z = y + 1
            if s[y] == s[z]:
                x = y
                while x - 1 >= 0 and z + 1 < len(s):
                    if s[x-1] == s[z+1]:
                        x -=1
                        z += 1
                    else:
                        break
                if len(l) < z - x + 1:
                    l = s[x:z+1]
            y += 1
            z = y + 1
        return l