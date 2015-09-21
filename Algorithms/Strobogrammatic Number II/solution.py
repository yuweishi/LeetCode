class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        start = {'6': '9', '9': '6', '8': '8', '1': '1'}
        even = {'6': '9', '9': '6', '0': '0', '8': '8', '1': '1'}
        odd = {'0': '0', '8':'8', '1': '1'}
        if n < 2:
            return self.generate(n, even, odd)
        return [key + num + value for key, value in start.items() for num in self.generate(n - 2, even, odd)]
        
    def generate(self, n, even, odd):
        if n == 0:
            return ['']
        if n == 1:
            return [key for key in odd]
        return [key + num + value for key, value in even.items() for num in self.generate(n - 2, even, odd)]
