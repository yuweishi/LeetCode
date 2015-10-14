class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit1, low, high = self.check(prices)
        profit2 = max(self.check(prices[:low])[0], self.check(prices[high:])[0])
        profit3 = self.check(map(lambda x: -x, prices[low: high]))[0] if profit1 else 0
        return profit1 + max(profit2, profit3)
    
    def check(self, prices):
        low_temp, low, high = 0, 0, len(prices) - 1
        profit = 0
        for i in xrange(len(prices)):
            dif = prices[i] - prices[low_temp]
            if dif < 0:
                low_temp = i
            elif dif > profit:
                low = low_temp
                high = i
                profit = dif
        return profit, low, high + 1
