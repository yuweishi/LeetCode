class Solution(object):
    #Method 1: General iterative way by compare every str with
    #current longest common prefix
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        pre = strs[0]
        for str in strs[1:]:
            if len(pre) > len(str):
                pre, str = str, pre
            for i in range(len(pre)):
                if pre[i] != str[i]:
                    pre = pre[0:i]
                    break
            if not pre:
                return ''
        return pre

    #Method 2: Pythonic way using zip
    def longestCommonPrefix(self, strs):
        prefix = ''
        # * is the unpacking operator, essential here
        for z in zip(*strs):
            bag = set(z)
            if len(bag) == 1:
                prefix += bag.pop()
            else:
                break
        return prefix
