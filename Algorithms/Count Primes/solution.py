class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        #trick 1: avoid even number except 2
        sign, real_n, n = (int(n ** 0.5) + 1)/2, n, (n / 2)
        primes = [1] * n
        #trick 2: use sqrt(n) to constraint search
        for i in range(1, sign):
            if primes[i]:
                #trick 3: use i * i as start
                real_i = (2 * i) + 1
                multi = real_i ** 2 / 2
                primes[multi: n: real_i] = [False] * len(primes[multi: n: real_i])
        return sum(primes)
