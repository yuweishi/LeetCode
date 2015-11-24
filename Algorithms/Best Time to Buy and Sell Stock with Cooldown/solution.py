class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy = noact = float("-inf")
        sell = cooldown = 0
        for price in prices:
            pre = sell
            sell = max(sell, noact + price)
            buy = cooldown - price
            noact = max(noact, buy)
            cooldown = pre
        return sell
