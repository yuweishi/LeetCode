class Solution(object):
    def canPermutePalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = collections.defaultdict(int)
        for char in s:
            dict[char] += 1
        count = 0
        for key in dict:
            if dict[key] % 2:
                count += 1
        return count < 2
