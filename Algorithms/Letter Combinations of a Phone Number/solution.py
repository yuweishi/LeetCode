class Solution(object):
    #Method 1: general iterative method
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        pad = {'0':' ', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = ['']
        for char in digits:
            new = []
            for num in pad[char]:
                for pre in res:
                    new += [pre + num]
            res = new
        return res
    
    #Method 2: Pythonic iterative method
    def letterCombinations(self, digits):
        if not digits:
            return []
        pad = {'0':' ', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        return reduce(lambda acc, digit: [x + y for x in acc for y in pad[digit]], digits, [''])

    #Method 3: backtracking method
    def letterCombinations(self, digits):
        pad = {'0':' ', '1':'', '2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
        res = []
        if digits:
            self.generate(res, pad, '', digits)
        return res
    def generate(self, res, pad, pre, digits):
        if digits:
            strs = pad[digits[0]]
            digits = digits[1:]
            for char in strs:
                self.generate(res, pad, pre + char, digits)
            if strs == '':
                self.generate(res, pad, pre, digits)
        else:
            res += [pre]"""
