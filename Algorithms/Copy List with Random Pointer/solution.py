class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return head
        #copy by p->p'->p->p'->p->p'
        p = head
        while p:
            next = p.next
            p.next = RandomListNode(p.label)
            p.next.next = next
            p = next
        #copy random pointers    
        p = head
        while p:
            if p.random:
                p.next.random = p.random.next
            p = p.next.next
        #split two list    
        copy = head.next
        p = head
        while p.next.next:
            next = p.next.next
            p.next.next = next.next
            p.next = next
            p = next
        p.next = None
        return copy
