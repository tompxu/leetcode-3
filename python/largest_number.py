class Solution:
    # @param num, a list of integers
    # @return a string
    def largestNumber(self, num):
        def compare(a, b):
            if a+b > b+a:
                return 1
            elif a+b < b+a
                return -1
            else:
                return 0

        def sort(array):
            less = []
            equal = []
            greater = []
            if len(array) > 1:
                pivot = array[0]
                for x in array:
                    i = compare(x, pivot)
                    if i == -1:
                        less.append(x)
                    if i == 0:
                        equal.append(x)
                    if i == 1:
                        greater.append(x)
                return sort(greater)+equal+sort(less) 
            else:  
                return array
        num = [str(i) for i in num]
        num = sort(num)
        num = "".join(num)
        if len(num.lstrip("0")) == 0:
            return "0"
        else:
            return num