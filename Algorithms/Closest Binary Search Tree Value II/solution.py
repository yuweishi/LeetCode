class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        """
        res, pre, suc = [], [], []
        self.inorder(root, target, False, pre)
        self.inorder(root, target, True, suc)
        while k:
            if not pre:
                res += [suc.pop()]
            elif not suc:
                res += [pre.pop()]
            else:
                res += [pre.pop()] if (target - pre[-1]) < (suc[-1] - target) else [suc.pop()]
            k -= 1
        return res
    def inorder(self, root, target, reverse, stack):
        if not root:
            return
        self.inorder(root.right if reverse else root.left, target, reverse, stack)
        if reverse and root.val <= target or not reverse and root.val > target:
            return
        stack.append(root.val)
        self.inorder(root.left if reverse else root.right, target, reverse, stack)
