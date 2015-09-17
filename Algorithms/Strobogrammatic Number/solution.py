class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        dict = {'6': '9', '9': '6', '0': '0', '8':'8', '1': '1'}
        start, end = 0, len(num) - 1
        while start <= end:
            if num[end] not in dict or num[start] != dict[num[end]]:
                return False
            start, end = start + 1, end - 1
        return True
