class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        dummy.next = head
        pre = dummy
	#Pre.next represent current value, if cur is unique: cur becomes pre; else next becomes cur
        while pre.next:
            next = pre.next.next
            while next and next.val == pre.next.val:
                next = next.next
            if next == pre.next.next:
                pre = pre.next
            else:
                pre.next = next
        pre.next = None
        return dummy.next
