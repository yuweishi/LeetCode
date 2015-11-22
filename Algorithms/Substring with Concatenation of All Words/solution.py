class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or len(s) < len(words[0]):
            return []
        n, Origin, res = len(words[0]), collections.Counter(words), []
        for end in xrange(n):
            start, missing, Map = end, len(words), collections.defaultdict(int)
            while end <= len(s) - n:
                cur = s[end: end + n]
                if cur in Origin:
                    Map[cur] += 1
                    missing -= 1
                    while Map[cur] > Origin[cur]:
                        Map[s[start: start + n]] -= 1
                        missing += 1
                        start += n
                    if missing == 0:
                        res += [start]
                else:
                    start, missing, Map = end + n, len(words), collections.defaultdict(int)
                end += n
        return res
