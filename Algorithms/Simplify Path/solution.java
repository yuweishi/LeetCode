public class Solution {
    public String simplifyPath(String path) {
        Stack<String> stack = new Stack<String>();
        String[] path_split = path.split("/", -1);
        for (String cur: path_split) {
            if (cur.equals("..")) {
                if (!stack.isEmpty()) 
                    stack.pop();
            }
            else if (!cur.equals("") && !cur.equals("."))
                stack.push(cur);
        }
        String res = "";
        while (!stack.isEmpty()) {
            res = "/" + stack.pop() + res;
        }
        return res.equals("") ? "/" : res;
    }
}
