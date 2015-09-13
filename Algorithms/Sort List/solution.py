class Solution(object):
    #Method 1: Merge sort, divide and conquer
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        fast = slow.next
        slow.next = None
        return self.merge(self.sortList(head), self.sortList(fast))
    def merge(self, l1, l2):
        dummy = p = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        if l1:
            p.next = l1
        else:
            p.next = l2
        return dummy.next
    #Method 2: Quick sort
    def sortList(self, head):
        return self.quicksort(head)[0]
    def quicksort(self, head):
        if not head or not head.next:
            return head, head
        #divide head into [small.next, ps] + [head, pe] + [large.next, pl]
        pl = large = ListNode(0)
        ps = small = ListNode(0)
        pe, p = head, head.next
        while p:
            if p.val < head.val:
                ps.next = p
                ps = ps.next
            elif p.val > head.val:
                pl.next = p
                pl = pl.next
            else:
                pe.next = p
                pe = pe.next
            p = p.next
        #Cut out small&large, repeat quick sort and return [small.next, ends], [large.next, endl]
        ps.next = None
        pl.next = None
        pe.next = None
        small.next, ends = self.quicksort(small.next)
        large.next, endl = self.quicksort(large.next)
        #Check whether small exists, and link it with equal
        if ends == None:
            small.next = head
        else:
            ends.next = head
        #Check whether large exists, and link it with equal
        if endl == None:
            endl = pe
        else:
            pe.next = large.next
        return small.next, endl
