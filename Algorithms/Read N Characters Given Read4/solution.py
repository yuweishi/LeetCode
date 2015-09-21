# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        index = 0
        while True:
            buf4 = [''] * 4
            size = min(read4(buf4), n)
            for i in range(size):
                buf[index] = buf4[i]
                index += 1
            if size < 4:
                return index
            n -= 4
