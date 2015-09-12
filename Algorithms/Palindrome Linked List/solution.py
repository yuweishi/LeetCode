class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast, mid = head, head, None
        while fast and fast.next:
            next = slow.next
            fast = fast.next.next
            slow.next = mid
            mid = slow
            slow = next
        #total number of nodes n is odd, mid stops in (n - 1) / 2, slow stops in (n + 1) / 2 
        #otherwise, n is even, mid stops in n / 2, slow stops in n / 2 + 1
        if fast:
            slow = slow.next
        while mid:
            if mid.val != slow.val:
                return False
            mid = mid.next
            slow = slow.next
        return True
