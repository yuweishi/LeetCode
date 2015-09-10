class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
            if slow == fast:
                fast = head
                while True:
                    if fast == slow:
                        return fast
                    fast = fast.next
                    slow = slow.next
        return None
