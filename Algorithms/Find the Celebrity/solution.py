# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        #Method 1: Bruce force
        res = -1
        for a in range(n):
            for b in range(n):
                if a == b: continue
                if (knows(a, b), knows(b, a)) != (False, True): break
            else: return a    
        return res

	#Method 2: Two pass
        candidate = 0;
        for i in range(n):
            if knows(candidate, i): candidate = i
        for i in range(n):
            if i != candidate and (knows(candidate, i) or not knows(i, candidate)): return -1
        return candidate
