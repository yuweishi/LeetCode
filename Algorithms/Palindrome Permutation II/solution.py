class Solution(object):
    def generatePalindromes(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        dict = collections.defaultdict(int)
        for char in s:
            dict[char] +=1
        odd = ''
        str = ''
        for k, v in dict.items():
            str += k * (v / 2)
            if v % 2:
                if odd:
                    return []
                odd = k
        return [p + odd + p[::-1] for p in self.permuteUnique(str)]
        
    def permuteUnique(self, nums):
        return [nums[i] + p
        for i in range(len(nums)) if i == 0 or nums[i] != nums[i - 1]
        for p in self.permuteUnique(nums[:i] + nums[i + 1:])] or ['']
