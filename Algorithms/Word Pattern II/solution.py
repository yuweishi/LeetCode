class Solution(object):
    def wordPatternMatch(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        return self.match(pattern, str, 0, 0, {}, set())
    def match(self, pattern, str, index, start, dict, set):
        #reach the end, return True
        if start == len(str) and index == len(pattern): return True
        #cannot reach the end at the same time, return False
        if index == len(pattern) or len(str) - start < len(pattern) - index: return False
        #check if current pattern already exist
        cur_pattern = pattern[index]
        #if exist, check whether match
        if cur_pattern in dict:
            p = dict[cur_pattern]
            if p != str[start: start + len(p)]:
                return False
            return self.match(pattern, str, index + 1, start + len(p), dict, set)
        #otherwise, try to find a new pattern
        for end in xrange(start + 1, len(str) + 1):
            substr = str[start: end]
            #check whether a substr may refer to two different pattern
            if substr not in set:
                dict[cur_pattern] = substr
                set.add(substr)
                if self.match(pattern, str, index + 1, end, dict, set):
                    return True
                del dict[cur_pattern]
                set.remove(substr)
        return False
