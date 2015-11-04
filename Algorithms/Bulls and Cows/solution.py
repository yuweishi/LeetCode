class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        count1 = count2 = 0
        map = collections.defaultdict(int)
        for i in xrange(len(secret)):
            if secret[i] == guess[i]:
                count1 += 1
            else:
                if map[secret[i]] < 0: count2 += 1
                if map[guess[i]] > 0: count2 += 1
                map[secret[i]] += 1
                map[guess[i]] -= 1
        return str(count1) + "A" + str(count2) + "B"
