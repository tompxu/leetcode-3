class Solution:
    # @param version1, a string
    # @param version2, a string
    # @return an integer
    def compareVersion(self, version1, version2):
        def compare(a, b):
            if a > b:
                return 1
            elif a < b:
                return -1
            else:
                return 0
                
        def removeZero(l):
            while len(l) >0 and l[-1] == 0:
                l.pop()
            return l


        v1 = removeZero([int(i) for i in version1.split(".")])
        v2 = removeZero([int(i) for i in version2.split(".")])
        
        if v1 == v2:
            return 0

        l = min([len(v1), len(v2)])
        for i in range(l):
            result = compare(v1[i], v2[i])
            if result == 0:
                continue
            else:
                return result
        if len(v1) > len(v2):
            return 1
        else:
            return -1