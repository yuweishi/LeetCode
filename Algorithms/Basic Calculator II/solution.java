public class Solution {
    public int calculate(String s) {
        int res = 0, num = 0;
        char sign = '+';
        Stack<Integer> stack = new Stack<Integer>();
        s += '+';
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (Character.isDigit(c))
                num = num * 10 + c - '0';
            else if (c != ' ') {
                switch(sign) {
                    case '+':
                        stack.push(num);
                        break;
                    case '-':
                        stack.push(-num);
                        break;
                    case '*':
                        stack.push(stack.pop() * num);
                        break;
                    case '/':
                        int pre = stack.pop();
                        stack.push(pre / num);
                }
                sign = c;
                num = 0;
            }
        }
        while (!stack.empty()) 
            res += stack.pop();
        return res;
    }
}
