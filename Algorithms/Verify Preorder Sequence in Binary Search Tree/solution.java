public class Solution {
    public boolean verifyPreorder(int[] preorder) {
        int low = Integer.MIN_VALUE;
        Stack<Integer> pre = new Stack();
        for (int node: preorder) {
            if (node <= low) 
                return false;
            while (!pre.empty() && node > pre.peek())
                low = pre.pop();
            pre.push(node);
        }
        return true;
    }
}
