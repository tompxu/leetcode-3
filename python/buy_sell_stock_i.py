class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <= 1:
            return 0
        minPrice = 0
        maxPrice = 1
        temp_min = 0
        for i in xrange(1,len(prices)):
            if prices[i] < prices[temp_min]:
                temp_min = i
            if prices[i] > prices[maxPrice]:
                maxPrice = i
            if (prices[i] - prices[temp_min]) > prices[maxPrice] - prices[minPrice]:
                minPrice = temp_min
                maxPrice = i
        if prices[maxPrice] - prices[minPrice] > 0:
            return prices[maxPrice] - prices[minPrice]
        else:
            return 0