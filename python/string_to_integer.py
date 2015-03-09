class Solution:
    # @return an integer
    def atoi(self, str):
        result = []
        positive = 1
        str = str.lstrip()
        value = {'+':1, '-': -1}
        if len(str) < 1:
            return 0
        if ord(str[0]) not in range(ord('0'), ord('9')+1) and str[0] not in ['+','-']:
            return 0
        else:
            for i in range(len(str)):
                if ord(str[i]) in range(ord('0'), ord('9')+1):
                    result.append(str[i])
                elif str[i] in ['+','-']:
                    if i == 0:
                        positive = positive * value[str[i]]
                    else:
                        break
                else:
                    break
        if len(result) == 0:
            return 0
        result = int("".join(result)) * positive
        if result > 2147483647:
            return 2147483647
        elif result < -2147483648:
            return -2147483648
        else:
            return result