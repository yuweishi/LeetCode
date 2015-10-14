class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        if k == 0 or prices == []:
            return 0
        if k > len(prices) / 2:
            return sum([prices[i] - prices[i - 1] for i in xrange(1, len(prices)) if prices[i] > prices[i - 1]])
        buy = [float("-Inf")] * k
        sell = [0] * k
        for price in prices:
            for i in xrange(k - 1, 0, -1):
                sell[i] = max(sell[i], price + buy[i])
                buy[i] = max(buy[i], sell[i - 1] - price)
            sell[0] = max(sell[0], price + buy[0])
            buy[0] = max(buy[0], -price)
        return sell[-1]
