class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ListSort = ListNode(0)
        p = ListSort
        while head:
            next = head.next
            while p.next and p.next.val < head.val:
                p = p.next
            head.next = p.next
            p.next = head
            if next and next.val>=head.val:#not necessary, it is used to avoid TLE
                p = head
            else:
                p = ListSort
            head = next
        return ListSort.next
