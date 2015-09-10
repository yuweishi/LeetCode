class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        new = None
        while head:
            next = head.next
            head.next = new
            new = head
            head = next
        return new
