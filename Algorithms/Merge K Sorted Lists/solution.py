class Solution(object):
    #Method 1: recursive using merge two
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        while len(lists) > 1:
            a = lists.pop(0)
            b = lists.pop(0)
            lists += [self.mergeTwoLists(a, b)]
        return lists[0] if lists else lists
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(None)
        l = dummy
        while l1 and l2:
            if l1.val <= l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            l = l.next
        if l1:
            l.next = l1
        else:
            l.next = l2
        return dummy.next
    #Method 2: using minHeap
    def mergeKLists(self, lists):
        if not lists:
            return None
        #Create minHeap
        dummyNode = cur = ListNode(0)
        minHeap = [(l.val, l) for l in lists if l]
        heapq.heapify(minHeap)
        #find minimum by heappop
        while minHeap:
            cur.next = heapq.heappop(minHeap)[1]
            cur = cur.next
            #if minimum.next exist, add it to minHeap
            if cur.next:
                heapq.heappush(minHeap, (cur.next.val, cur.next))
        return dummyNode.next
