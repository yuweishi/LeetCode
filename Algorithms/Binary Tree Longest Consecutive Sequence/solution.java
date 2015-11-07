/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    private int max = 0;
    public int longestConsecutive(TreeNode root) {
        find(root, 0, 0);
        return max;
    }
    
    private void find(TreeNode root, int pre, int count) {
        if (root == null) return;
        count = (count != 0 && root.val != pre + 1) ? 1: count + 1;
        max = Math.max(max, count);
        find(root.left, root.val, count);
        find(root.right, root.val, count);
    }
}
