class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """
        groups = collections.defaultdict(list)
        for s in strings:
            groups[tuple(map(lambda x: (ord(x) - ord(s[0])) % 26, s))] += s,
        return map(sorted, groups.values())
