class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        min1_old = min2_old = 0
        for i in range(len(costs)):
            min1 = min2 = float('Inf')
            for j in range(len(costs[0])):
                if costs[i - 1][j] == min1_old:
                    costs[i][j] += min2_old
                else:
                    costs[i][j] += min1_old
                if costs[i][j] <= min1:
                    min2 = min1
                    min1 = costs[i][j]
                elif costs[i][j] < min2:
                    min2 = costs[i][j]
            min1_old, min2_old = min1, min2
        return min1_old
