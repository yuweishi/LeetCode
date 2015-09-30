class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        #return directly if nothing remain
        if numerator % denominator == 0:
            return str(numerator / denominator)
        #else, add sign, integer part and dot
        res =  '-' if (numerator < 0) ^ (denominator < 0) else ''
        dict, numerator, denominator = {}, abs(numerator), abs(denominator)
        res += str(numerator / denominator) + '.'
        remainder, i = numerator % denominator, len(res)
        while remainder:
            if remainder in dict:
                return res[:dict[remainder]] + '(' + res[dict[remainder]:] + ')'
            dict[remainder] = i
            i += 1
            remainder *= 10
            res += str(remainder / denominator)
            remainder %= denominator
        return res
