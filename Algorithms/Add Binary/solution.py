class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res, flag, i = '', 0, 1
        while i <= len(a) or i <= len(b) or flag:
            diga = 0 if i > len(a) else int(a[-i])
            digb = 0 if i > len(b) else int(b[-i])
            res = str(digb ^ diga ^ flag) + res
            if digb + diga + flag > 1:
                flag = 1
            else:
                flag = 0
            i += 1
        return res
