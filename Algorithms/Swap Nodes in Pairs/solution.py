class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
	#Method 1: swap one by one
        dummy = ListNode(0)
        node1, node2 = head, dummy
        while node1:
            if node1.next:
                node2.next = node1.next
                node1.next = node1.next.next
                node2.next.next = node1
                node2 = node1
            else:
                node2.next = node1
            node1 = node1.next
        return dummy.next
	
	#Method 2: recursive
        if head and head.next:
            first = head.next
            head.next = self.swapPairs(first.next)
            first.next = head
            return first
        return head
