class Solution(object):
    #Method 1: recursive
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        n = len(num)
        for i in xrange(1, n / 2 + 1):
            for j in xrange(i + 1, i + (n - i) / 2 + 1):
                if self.additive(num[:i], num[i: j], num[j:]):
                    return True
                if num[i] == '0' and j > i:
                    break
            if num[0] == '0' and i > 0:
                break
        return False
    def additive(self, num1, num2, num3):
        x = int(num1) + int(num2)
        if x == int(num3) and not (num3[0] == '0' and len(num3) != 1):
            return True
        for i in xrange(1, len(num3) / 2 + 1):
            if num3[0] == '0' and i > 1:
                break
            if x != int(num3[:i]):
                continue
            if self.additive(num2, num3[:i], num3[i:]):
                return True
        return False

    #Method 2: iterative
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        n = len(num)
        for i in xrange(1, n / 2 + 1):
            for j in xrange(i + 1, i + (n - i) / 2 + 1):
                start1, start2, start3 = 0, i, j
                while start3 < n:
                    cur = str(int(num[start1: start2]) + int(num[start2: start3]))
                    if num[start3:].startswith(cur):
                        start1, start2, start3 = start2, start3, start3 + len(cur)
                    else:
                        break
                if n == start3:
                    return True
                if num[i] == '0' and j > i:
                    break
            if num[0] == '0' and i > 0:
                break
        return False
