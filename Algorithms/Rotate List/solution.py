class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        #get length
        i, p = 0, head
        while p:
            i += 1
            p = p.next
        #mod and check
        if not i or not k % i:
            return head
        #rotate in one pass using two pointers
        k %= i
        late, early = head, head
        while early.next:
            if k:
                k -= 1
            else:
                late = late.next
            early = early.next
        early.next = head
        head = late.next
        late.next = None
        return head
