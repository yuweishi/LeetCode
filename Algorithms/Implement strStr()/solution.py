class Solution:
    # @param {string} haystack
    # @param {string} needle
    # @return {integer}
    def strStr(self, haystack, needle):
        #Method 1: brute force
	if not haystack and not needle:
            return 0
        for i in range(0, len(haystack) - len(needle) + 1):
            for j in range(i, len(haystack) + 1):
                if j - i == len(needle):
                    return i
                if needle[j - i] != haystack[j]:
                    break
        return -1

	#Method 2: KMP
        if not haystack and not needle:
            return 0
        #generate next array, need O(n) time
        i, j, m, n = -1, 0, len(haystack), len(needle)
        next = [-1] * n
        while j < n - 1:  
            #needle[k] stands for prefix, neelde[j] stands for postfix
            if i == -1 or needle[i] == needle[j]:   
                i, j = i + 1, j + 1
                next[j] = i
            else:
                i = next[i]
        #check through the haystack using next, need O(m) time
        i = j = 0
        while i < m and j < n:
            if j == -1 or haystack[i] == needle[j]:
                i, j = i + 1, j + 1
            else:
                j = next[j]
        if j == n:
            return i - j
        return -1
