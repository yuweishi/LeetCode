class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        #Method 1: iterative
        min, dif = None, float('Inf')
        while root:
            if abs(target - root.val) < dif:
                min, dif = root.val, abs(target - root.val)
            if root.val < target:
                root = root.right
            else:
                root = root.left
        return min
        #Method 2: recursive
	if not root:
            return float('Inf')
        next = root.left if root.val > target else root.right
        min = self.closestValue(next, target)
        return root.val if abs(root.val - target) < abs(target - min) else min
