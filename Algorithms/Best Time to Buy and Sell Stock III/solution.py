class Solution(object):
    #Method1: go through twice
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

    #Method 2: DP
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy1 = buy2 = float("-Inf")
        sell1 = sell2 = 0
        for price in prices:
            sell2 = max(sell2, price + buy2)
            buy2 = max(buy2, sell1 - price)
            sell1 = max(sell1, price + buy1)
            buy1 = max(buy1, -price)
        return sell2
