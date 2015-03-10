class Solution:
    # @param num, a list of integers
    # @return an integer
    def majorityElement(self, num):
        num = list(sorted(num))
        return num[len(num)/2]