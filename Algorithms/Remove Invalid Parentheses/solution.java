public class Solution {
    public List<String> removeInvalidParentheses(String s) {
        List<String> res = new ArrayList<>();
        if (s == null) return res;
        Set<String> visited = new HashSet<>(); visited.add(s);
        Queue<String> queue = new LinkedList<>(); queue.add(s);
        boolean found = false;

        while (!queue.isEmpty()) {
            s = queue.poll();
            char balance = isValid(s);
            if (balance == '0') {
                // found an answer, add to the result
                res.add(s);
                found = true;
            }
            if (!found) {
                // generate all possible states
                for (int i = 0; i < s.length(); i++) {
                    // we only try to remove left or right paren
                    if (s.charAt(i) == balance) {
                        String t = s.substring(0, i) + s.substring(i + 1);
                        if (!visited.contains(t)) {
                            // for each state, if it's not visited, add it to the queue
                            queue.add(t);
                            visited.add(t);
                        }
                    }
                }
            }
        }
        return res;
    }

    // helper function checks if string s contains valid parantheses
    private char isValid(String s) {
        int count = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') count++;
            if (c == ')' && count-- == 0) return ')';
        }
        return count == 0 ? '0': '(';
    }
}
