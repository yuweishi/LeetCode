class WordDistance(object):
    def __init__(self, words):
        """
        initialize your data structure here.
        :type words: List[str]
        """
        self.map = collections.defaultdict(list)
        for i in range(len(words)):
            self.map[words[i]] += [i]

    def shortest(self, word1, word2):
        """
        Adds a word into the data structure.
        :type word1: str
        :type word2: str
        :rtype: int
        """
        dist1, dist2 = self.map[word1], self.map[word2]
        dist = float('Inf')
        p1, p2 = len(dist1) - 1, len(dist2) - 1
        while p1 >= 0 and p2 >= 0:
            dist = min(dist, abs(dist1[p1] - dist2[p2]))
            if dist1[p1] >= dist2[p2]:
                p1 -= 1
            else:
                p2 -= 1
        return dist 

# Your WordDistance object will be instantiated and called as such:
# wordDistance = WordDistance(words)
# wordDistance.shortest("word1", "word2")
# wordDistance.shortest("anotherWord1", "anotherWord2")
