class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        count, n = 0, len(citations)
        array =  [0] * (n + 1)
        for num in citations:
            if num >= n:
                array[n] += 1
            else:
                array[num] += 1
        
        for i in xrange(n, -1, -1):
            count += array[i]
            if count >= i:
                return i
