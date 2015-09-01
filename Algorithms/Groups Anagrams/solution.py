class Solution(object):
    #Method 1: Regular Method
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        res = []
        for str in strs:
            new = ''.join(sorted(str))
            if new not in dict:
                dict[new] = len(res)
                res += [[]]
            res[dict[new]] += [str]
        for i in range(len(res)):
            res[i].sort()
        return res
    #Pythonic way using map() and collections.defaultdict()
    def groupAnagrams(self, strs):
        groups = collections.defaultdict(list)
        for s in strs:
            groups[tuple(sorted(s))].append(s)
        return map(sorted, groups.values())
