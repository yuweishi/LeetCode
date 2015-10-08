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
    int count = 0;
    boolean left, right;
    public int countUnivalSubtrees(TreeNode root) {
        check(root);
        return count;
    }
    private boolean check(TreeNode root){
        if (root == null) return true;
        left = check(root.left);
        right = check(root.right);
        if (!left || !right || root.left != null && root.left.val != root.val || root.right != null && root.right.val != root.val) return false;
        count++;
        return true;
    }
}
