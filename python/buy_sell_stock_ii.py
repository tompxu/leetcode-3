class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        if len(prices) <=1:
            return 0
        total = 0
        for i in range(1,len(prices)):
            if prices[i-1] < prices[i]:
                total = total + prices[i] - prices[i-1]
        return total