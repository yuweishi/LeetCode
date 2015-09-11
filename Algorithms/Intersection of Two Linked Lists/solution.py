class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if not headA or not headB:
            return None
        pA, pB, flag = headA, headB, 0
        while pA and pB:
            if pA == pB:
                return pA
            if pA.next:
                pA = pA.next
            else:
                pA = headB
                if flag == 0:
                    flag = 1
                else:
                    return None
            if pB.next:
                pB = pB.next
            else:
                pB = headA
