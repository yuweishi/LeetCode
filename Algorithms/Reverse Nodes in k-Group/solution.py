class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    def reverseKGroup(self, head, k):
        #get the length
        p = head
        i = 0
        while p and i < k:
            i += 1
            p = p.next
        #pre check. if len < k, return directly
        if k == 1 or i < k:
            return head
        #otherwise, reverse firt part
        start, end = None, head
        while head != p:
            next = head.next
            head.next = start
            start = head
            head = next
        end.next = self.reverseKGroup(head, k)
        return start
