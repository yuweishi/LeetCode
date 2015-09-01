class Solution(object):
    def convert(self, s, numRows):
        """
            :type s: str
            :type numRows: int
            :rtype: str
            """
        if numRows == 1:
            return s
        array = [''] * numRows
        cur, step = 0, -1
        for char in s:
            array[cur] += char
            if cur in [0, numRows - 1]:
                step = -step
            cur += step
        res = ''
        for item in array:
            res += item
        return res