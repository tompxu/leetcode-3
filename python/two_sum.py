class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        temp = {}
        result = -1
        for i in range(len(num)):
            if num[i] not in temp:
                temp[num[i]] = [i]
            else:
                temp[num[i]].append(i)
        for i in range(len(num)):
            t = target - num[i]
            if t in temp:
                if temp[t][0] == i:
                    if len(temp[t]) > 1:
                        result = temp[t][1]
                else:
                    result = temp[t][0]
            if result >= 0:
                if result > i:
                    return (i+1, result+1)
                elif result < i:
                    return (result+1, i+1)
                else:
                    pass