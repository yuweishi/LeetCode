public class Solution {
    public boolean isValid(String s) {
        Stack <Character> stack = new Stack<>();
        HashMap <Character, Character> map = new HashMap<>();
        map.put('(', ')');
        map.put('{', '}');
        map.put('[', ']');

        for (int i = 0; i < s.length(); i++){
            if (map.containsKey(s.charAt(i)))
                stack.push(map.get(s.charAt(i)));
            else{
                if (stack.empty() || stack.pop() != s.charAt(i))
                    return false;
            }
        }
        return stack.empty();
    }
}
