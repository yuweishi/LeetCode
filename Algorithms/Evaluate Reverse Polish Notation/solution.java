public class Solution {
    public int evalRPN(String[] tokens) {
        HashSet<String> ope = new HashSet<String>();ope.add("+");ope.add("-");ope.add("/");ope.add("*");
        int a, b, res;
        Stack<Integer> stack = new Stack<Integer>();
        for (String item : tokens) {
            if (ope.contains(item)) {
                b = stack.pop();
                a = stack.pop();
                if (item.equals("-"))
                    res = a - b;
                else if (item.equals("+"))
                    res = a + b;
                else if (item.equals("*"))
                    res = a * b;
                else
                    res = a / b;
                stack.add(res);
            }
            else
                stack.add(Integer.parseInt(item));
        }
        return stack.pop();
    }
}
