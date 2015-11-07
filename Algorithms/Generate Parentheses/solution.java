public class Solution {
    public List<String> generateParenthesis(int n) {
        return generate(new ArrayList<String>(), 0, n, "");
    }
    public ArrayList<String> generate(ArrayList<String> res, int right, int left, String pre) {
        if (left == 0){
            for (int i = 0; i < right; i++) {
                pre = pre + ')';
            }
            res.add(pre);
        }
        else {
            generate(res, right + 1, left - 1, pre + '(');
            if (right > 0)
                generate(res, right - 1, left, pre + ')');
        }
        return res;
    }
}
