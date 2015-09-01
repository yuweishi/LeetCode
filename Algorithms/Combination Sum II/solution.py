class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        self.check(sorted(candidates), target, res, [])
        return res
    #Method 1: do not use for loop, for a sequence [1, 1, 1], we take[111, 11, 1], if 111 stop at 1, 
    #then check for duplicates when we try to add 1(11 stop at 1, 1stop at 1) again.
    def check(self, candidates, target, res, pre):
        #check if there's a duplicate, otherwise add pre to result
        if target == 0 and (not res or pre != res[-1]):
            res += [pre]
        if candidates and target >= candidates[0]:
            self.check(candidates[1:], target - candidates[0], res, pre + [candidates[0]])
            #check if cur is the begining of a sequence of [cur], if it is, cannot skip.
            if not pre or candidates[0] != pre[-1]:
                self.check(candidates[1:], target, res, pre)
    #Method 2: use for loop, so that for a sequence [1, 1, 1], only take[1XX, 11X, 111]. If match shows up early, stop
    def check(self, candidates, target, res, pre):
        if target == 0:
            res += [pre]
            return
        for i in range(len(candidates)):
            if candidates[i] > target:
                break
            if i == 0 or candidates[i] != candidates[i - 1]:
                self.check(candidates[i + 1:], target - candidates[i], res, pre + [candidates[i]])
    
