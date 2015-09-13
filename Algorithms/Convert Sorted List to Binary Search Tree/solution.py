class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        #Count the total number of nodes
        p, i = head, 0
        while p:
            p, i = p.next, i + 1
        return self.trans([head], i)
    def trans(self, list, n):
        if n < 1:
            return None
        if n == 1:
            val = list[0].val
            list[0] = list[0].next
            return TreeNode(val)
        mid = (n + 1) / 2
        root = TreeNode(0)
        root.left = self.trans(list, mid - 1)
        root.val = list[0].val
        list[0] = list[0].next
        root.right = self.trans(list, n - mid)
        return root
