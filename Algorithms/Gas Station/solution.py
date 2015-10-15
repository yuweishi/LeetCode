class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        start, pre, cur, n = 0, 0, 0, len(gas)
        for i in xrange(n):
            cur += gas[i] - cost[i]
            if cur < 0:
                pre += cur
                cur = 0
                start = i + 1
        return start if pre + cur >= 0 else -1
