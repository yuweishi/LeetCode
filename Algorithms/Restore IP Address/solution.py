class Solution(object):
    #Method 1: recursive using backtracking
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.generate(res, '', 4, s)
        return res
    def generate(self, res, pre, i, cur):
        if cur:
            if i == 1:
                if int(cur) < 256 and int(cur[0]) or len(cur) == 1 and cur[0] == '0':
                    res += [pre + cur]
            else:
                if len(cur) - 1 <= 3 * (i - 1):
                    self.generate(res, pre + cur[0] + '.', i - 1, cur[1:])
                if len(cur) - 2 >= (i - 1) and len(cur) - 2 <= 3 * (i - 1) and int(cur[0]):
                    self.generate(res, pre + cur[0:2] + '.', i - 1, cur[2:])
                if len(cur) - 3 >= (i - 1) and int(cur[0]) and int(cur[0:3]) < 256:
                    self.generate(res, pre + cur[0:3] + '.', i - 1, cur[3:])
    #Method 2: iterative using 3 for loop
    def restoreIpAddresses(self, s):
        res = []
        n = len(s)
        for i in range(max(1, n - 9), min(4, n - 2)):
            for j in range(max(i + 1, n - 6), min(i + 4, n - 1)):
                for k in range(max(j + 1, n - 3), min(j + 4, n)):
                    strs = (s[0:i], s[i:j], s[j:k], s[k:])
                    strs = [str for str in strs if len(str) == 1 or str[0] != '0' and int(str) < 256]
                    if len(strs) == 4:
                        res.append('.'.join(strs))
        return res
