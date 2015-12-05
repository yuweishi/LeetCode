class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1] + [float('inf')] * (n - 1)
        m = len(primes)
        index = [0] * m
        for i in xrange(1, n):
            for j in xrange(m):
                ugly[i] = min(ugly[i], primes[j] * ugly[index[j]])
            for j in xrange(m):
                if ugly[i] == primes[j] * ugly[index[j]]:
                    index[j] += 1
        return ugly[-1]
