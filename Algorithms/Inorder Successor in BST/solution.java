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
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        TreeNode suc = null;
        while (root != null) {
            if (p.val < root.val) {
                suc = root;
                root = root.left;
            }
            else {
                root = root.right;
            }
        }
        return suc;
    }
}
