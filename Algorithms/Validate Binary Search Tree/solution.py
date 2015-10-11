# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        list = []
        self.check(root, list)
        for i in xrange(1, len(list)):
            if list[i] <= list[i - 1]:
                return False
        return True
    def check(self, root, list):
        if not root:
            return
        self.check(root.left, list)
        list.append(root.val)
        self.check(root.right, list)
