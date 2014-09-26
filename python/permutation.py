class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    
    def permute(self, num):
        L = []
        def perm(n, begin,end):
	        if begin >= end:
		        L.append(list(n))
	        else:
		        for i in xrange(begin,end):
			        n[i],n[begin] = n[begin],n[i]
			        perm(n,begin+1,end)
			        n[i],n[begin] = n[begin],n[i]
        perm(num, 0, len(num))
        return L