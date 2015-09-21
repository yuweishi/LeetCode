class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #Method 1: two pointers
        start, end = 0, len(numbers) - 1
        while start < end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1
            elif sum < target:
                start += 1
            else:
                return start + 1, end + 1

	#Method 2: Binary search
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            tmp = target - numbers[i]
            while left <= right:
                mid = (left + right) // 2
                if numbers[mid] == tmp:
                    return i + 1, mid + 1
                elif numbers[mid] < tmp:
                    left = mid + 1
                else:
                    right = mid - 1
