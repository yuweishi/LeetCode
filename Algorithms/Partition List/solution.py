class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small, big = ListNode(0), ListNode(0)
        ps, pb = small, big
        while head:
            if head.val < x:
                ps.next = head
                ps = head
            else:
                pb.next = head
                pb = head
            head = head.next
        ps.next = big.next
        pb.next = None
        return small.next
