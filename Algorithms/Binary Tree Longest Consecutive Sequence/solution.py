# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        total = [0]
        self.find(root, 0, 0, total)
        return total[0]
    def find(self, root, pre, count, total):
        if not root:
            return
        if count != 0 and root.val != pre + 1:
            count = 1
        else:
            count += 1
        total[0] = max(total[0], count)
        self.find(root.left, root.val, count, total)
        self.find(root.right, root.val, count, total)
