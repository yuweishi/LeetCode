class Solution:
    # @param {ListNode} node
    # @return {void} Do not return anything, modify node in-place instead.
    def deleteNode(self, node):
        node.val = node.next.val
        if node.next.next:
            node.next = node.next.next
        else:
            node.next = None
