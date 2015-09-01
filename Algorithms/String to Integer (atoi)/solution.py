class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if str:
            #remove extra space
            str = str.split()[0]
            
            #remove sign and record
            sign = 1
            num = 0
            if str[0] == '-':
                sign = -1
                str = str[1:]
            elif str[0] == '+':
                str = str[1:]
        
            #check every digit and transfer
            for chr in str:
                if chr.isdigit():
                    num = num * 10 + int(chr)
                else:
                    break
            num *= sign
            
            #check overflow
            if num >= 1 << 31:
                return (1 << 31) - 1
            if num < - 1 << 31:
                return  -(1 << 31)
            return num
        return 0
