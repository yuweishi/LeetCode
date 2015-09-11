class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        for i in range(1, m):
            pre = pre.next
        end = pre.next
        head = end.next
        for i in range(n - m):
            end.next = head.next
            head.next = pre.next
            pre.next = head
            head = end.next
        return dummy.next
