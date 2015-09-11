class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        early, late = head, head
        while early:
            if n >= 0:
                n -= 1
            else:
                late = late.next
            early = early.next
        if n == 0:
            return head.next
        late.next = late.next.next
        return head
