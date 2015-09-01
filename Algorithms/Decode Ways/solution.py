class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        base1, base2, pre = 1, 1, s[0]
        for cur in s[1:]:
            num = int(pre + cur)
            if cur == '0' and (num > 26 or num == 0):
                #cannot decode, return 0
                return 0
            elif cur == '0':
                #must use int(pre + cur) rather than int(cur) to decode
                base1, base2 = 0, base1
            elif num <= 26 and num > 0:
                #both int(pre + cur) and int(cur) can be used to decode
                base1, base2 = base2, base1 + base2
            else:
                #must use int(cur) rather than int(pre + cur) to decode
                base1 = base2
            pre = cur
        return base2
