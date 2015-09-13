class Solution(object):
    def largestRectangleArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        left, right = self.sideview(height), self.sideview(height[::-1])[::-1]
        maximum = 0
        for i in range(n):
            cur = height[i] * (left[i] + right[i] - n)
            if cur > maximum:
                maximum = cur
        return maximum
    def sideview(self, nums):
        n = len(nums)
        stack, res = [], [0] * n
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                res[stack.pop()] = i
            stack.append(i)
        for i in stack:
            res[i] = n
        return res
