/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
public class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(0);
        ListNode l = dummy;
        while (l1 != null && l2 != null){
            if (l1.val <= l2.val){
                l.next = l1;
                l1 = l1.next;
            }
            else{
                l.next = l2;
                l2 = l2.next;
            }
            l = l.next;
        }
        if (l1 != null)
            l.next = l1;
        else
            l.next = l2;
        return dummy.next;
    }
}
