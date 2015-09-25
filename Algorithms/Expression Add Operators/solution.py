class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        """
        if not num:
            return []
        return self.generate([], num, target, '', 0, 0, 0)
    def generate(self, res, num, target, prefix, presum, prenum, pos):
        if len(num) == pos and target == presum:
            res.append(prefix)
        else:
            for i in range(pos + 1, len(num) + 1):
                cur = num[pos: i]
                curnum = int(cur)
                if pos == 0:
                    self.generate(res, num, target, cur, curnum, curnum, i)
                else:
                    self.generate(res, num, target, prefix + '+' + cur, presum + curnum, curnum, i)
                    self.generate(res, num, target, prefix + '-' + cur, presum - curnum, -curnum, i)
                    self.generate(res, num, target, prefix + '*' + cur, presum - prenum + prenum * curnum, prenum * curnum, i)
                if num[pos] == '0':
                    break
        return res
