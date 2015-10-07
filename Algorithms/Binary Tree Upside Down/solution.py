# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
	#Method 1: iterative using stack
        stack = []
        while root and root.left:
            stack.append(root)
            root = root.left
        res = root
        while stack:
            cur = stack.pop()
            root.left = cur.right
            root.right = cur
            cur.left = cur.right = None
            root = cur
        return res

	#Method 2: iterative without using stack
        pre = right = next = None
        while root:
            next = root.left
            root.left = right
            right = root.right
            root.right = pre
            pre = root
            root = next
        return pre

	#Method 3: Recursive
        if not root or not root.left:
            return root
        new = self.upsideDownBinaryTree(root.left)
        root.left.left = root.right
        root.left.right = root
        root.left = root.right = None
        return new
