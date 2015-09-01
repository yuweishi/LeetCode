class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        cur = '1'
        while n > 1:
            n -= 1
            pre, res = None, ''
            for char in cur:
                if char != pre:
                    if pre:
                        res += str(count) + pre
                    count = 1
                    pre = char
                else:
                    count += 1
            cur = res + str(count) + pre
        return cur
