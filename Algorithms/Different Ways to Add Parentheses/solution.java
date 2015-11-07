public class Solution {
    public List<Integer> diffWaysToCompute(String input) {
        List<Integer> res = new ArrayList<Integer>();
        for (int i = 0; i < input.length(); i++) {
            char cur = input.charAt(i);
            if (cur == '+' || cur == '*' || cur == '-') {
                List<Integer> left = diffWaysToCompute(input.substring(0, i));
                List<Integer> right = diffWaysToCompute(input.substring(i + 1));
                for (int x : left) {
                    for (int y: right) {
                        if (cur == '-')
                            res.add(x - y);
                        else if (cur == '+') 
                            res.add(x + y);
                        else
                            res.add(x * y);
                    }
                }
            }
        }
        if (res.size() == 0) 
            res.add(Integer.valueOf(input));
        return res;
    }
}
