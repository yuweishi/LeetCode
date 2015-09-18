public class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack<Integer>();
        int res = 0, num = 0, sign = 1;
        s = '(' + s + ')';
        for (int i = 0; i < s.length(); i++) {
            char chr = s.charAt(i);
            if (Character.isDigit(chr)) {
                num = num * 10 + (int) (chr - '0');
            }
            else if (chr == '-') {
                res += num * sign;
                num = 0;
                sign = -1;
            }
            else if (chr == '+') {
                res += num * sign;
                num = 0;
                sign = 1;
            }
            else if (chr == '(') {
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            }
            else if (chr == ')') {
                res += num * sign;
                res *= stack.pop();
                res += stack.pop();
                num = 0;
            }
        }
        return res;
    }
}
