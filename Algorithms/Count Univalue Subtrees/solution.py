# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        self.check(root, res)
        return res[0]
    def check(self, root, res):
        if not root:
            return True
        #shouldn't put it in flag, otherwise when left of and is not true, right part will not be executed
        left = self.check(root.left, res)
        right = self.check(root.right, res)
        flag = left and (not root.left or root.left.val == root.val) and right and (not root.right or root.right.val == root.val)
        if flag:
            res[0] += 1
        return flag
