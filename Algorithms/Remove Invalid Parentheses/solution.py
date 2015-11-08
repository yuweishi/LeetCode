class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        queue, res, visit, stop = [s], [], [], False
        while queue:
            cur = queue.pop(0)
            balance = self.valid(cur)
            if balance == '0':
                res += [cur]
                stop = True
            if not stop:
                for i in xrange(len(cur)):
                    if cur[i] == balance:
                        new = cur[:i] + cur[i + 1:]
                        if new not in visit:
                            visit += [new]
                            queue += [new]
        return res
            
    def valid(self, s):
        count = 0
        for char in s:
            if char == '(':
                count += 1
            if char == ')':
                if count == 0:
                    return ')';
                count -= 1
        return '0' if count == 0 else '('
