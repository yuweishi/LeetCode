class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
	#Method 1: use generator
        return [x + y if input[i] == '+' else (x - y if input[i] == '-' else x * y) for i in range(len(input)) if input[i] in '+-*' for x in self.diffWaysToCompute(input[:i]) for y in self.diffWaysToCompute(input[i + 1:])] or [int(input)]

	#Method 2: DP
