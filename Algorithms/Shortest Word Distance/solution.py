class Solution(object):
    def shortestDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = float('Inf')
        p1 = p2 = -1
        for i in range(len(words)):
            if words[i] == word1:
                p1 = i
            if words[i] == word2:
                p2 = i
            if p1 != -1 and p2 != -1:
                distance = min(distance, abs(p2 - p1))
        return distance
