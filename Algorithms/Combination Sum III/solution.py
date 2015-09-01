class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        self.check(1, n, res, [], k)
        return res
    def check(self, start, target, res, pre, k):
        if target == 0 and len(pre) == k:
            res += [pre]
            return
        if len(pre) == k or target == 0:
            return
        for i in range(start, 10):
            if target < i:
                break
            self.check(i + 1, target - i, res, pre + [i], k)
