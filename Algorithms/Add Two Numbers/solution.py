class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(0)
        p = res
        carry = 0
        while carry or l1 or l2:
            if l1:
                carry += l1.val 
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            p.next = ListNode(carry % 10)
            p = p.next
            carry = carry / 10
        return res.next
