class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = pre_buy = float("-inf")
        sell = pre_sell = 0
        for price in prices:
            pre_buy = buy
            buy = max(buy, pre_sell - price)
            pre_sell = sell
            sell = max(sell, pre_buy + price)
        return sell
