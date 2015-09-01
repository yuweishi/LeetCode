class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.check(sorted(candidates), target, res, [])
        return res
    #Method 1: check target before add [cur] to pre.
    def check(self, candidates, target, res, pre):
        if candidates:
            if target == candidates[0]:
                res += [pre + [target]]
            elif target > candidates[0]:
                self.check(candidates, target - candidates[0], res, pre + [candidates[0]])
                self.check(candidates[1:], target, res, pre)
    #Method 2: check target after pre add [cur].
    def check(self, candidates, target, res, pre):
        if target == 0:
            res += [pre]
        elif candidates and target >= candidates[0]:
            self.check(candidates[1:], target, res, pre)
            self.check(candidates, target - candidates[0], res, pre + [candidates[0]])
    #Method 3: use for loop
    def check(self, candidates, target, res, pre):
        if target == 0:
            res += [pre]
            return
        for i in range(len(candidates)):
            if target < candidates[i]:
                break
            self.check(candidates[i:], target - candidates[i], res, pre + [candidates[i]])
