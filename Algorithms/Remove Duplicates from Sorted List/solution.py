class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        start = head
        while start:
            end = start.next
            while end and start.val == end.val:
                end = end.next
            start.next = end
            start = start.next
        return head
