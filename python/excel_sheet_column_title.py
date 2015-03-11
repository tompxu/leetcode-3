class Solution:
    # @return a string
    def convertToTitle(self, num):
        if num == 0:
            return ""
        result = []
        while num > 0:
            result.append(chr(ord("A") + (num - 1) % 26))
            num = (num-1) / 26
        result = list(reversed(result))
        return "".join(result)