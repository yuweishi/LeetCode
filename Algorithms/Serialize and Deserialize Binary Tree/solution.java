/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Codec {
    
    // Encodes a tree to a single string.
    private void se(TreeNode root, StringBuilder sb){
        if (root == null)
            sb.append(',');
        else{
            sb.append(root.val).append(',');
            se(root.left, sb);
            se(root.right, sb);
        }
    }
    public String serialize(TreeNode root) {
        StringBuilder sb = new StringBuilder();
        se(root, sb);
        return sb.toString();
    }
    
    
    // Decodes your encoded data to tree.
    private TreeNode dese(Iterator nums){
        String cur = (String) nums.next();
        if (cur.length() == 0)
            return null;
        TreeNode root = new TreeNode(Integer.valueOf(cur));
        root.left = dese(nums);
        root.right = dese(nums);
        return root;
    }
    public TreeNode deserialize(String data) {
        Iterator nums = Arrays.asList(data.split(",", -2)).iterator();
        return dese(nums);
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));
