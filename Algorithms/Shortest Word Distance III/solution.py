class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        distance = float('Inf')
        p1 = p2 = -distance
        for i in range(len(words)):
            if words[i] == word1 and (word1 != word2 or p1 <= p2):
                p1 = i
            elif words[i] == word2:
                p2 = i
            distance = min(distance, abs(p2 - p1))
        return distance
