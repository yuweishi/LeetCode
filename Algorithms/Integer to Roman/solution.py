class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        base = 1000
        res =''
        dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
            }
        while num:
            dig = num / base
            if dig:
                if dig < 4:
                    res += dict[base] * dig
                elif dig == 4:
                    res += dict[base] + dict[5 * base]
                elif dig < 9:
                    res += dict[5 *base] +(dig % 5) * dict[base]
                else:
                    res += dict[base] + dict[10 * base]
            num %= base
            base /= 10
        return res
