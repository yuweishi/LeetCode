class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        #find the mid point of the list
        if not head: return
        slow, fast = head, head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        #reverse the second part of the list
        fast = slow.next
        slow.next = None
        reverse = None
        while fast:
            next = fast.next
            fast.next = reverse
            reverse = fast
            fast = next
        #return reorder list
        reorder = ListNode(0)
        p = reorder
        while reverse:
            p.next = head
            head = head.next
            p.next.next = reverse
            reverse = reverse.next
            p = p.next.next
        p.next = head
