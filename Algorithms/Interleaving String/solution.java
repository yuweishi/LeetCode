public class Solution {
    public boolean isInterleave(String s1, String s2, String s3) {
        //Method 1: DP
        int n1 = s1.length(), n2 = s2.length(), n3 = s3.length();
        if (n1 + n2 != n3) {
            return false;
        }
        boolean[][] dp = new boolean[n1 + 1][n2 + 1];
        dp[0][0] = true;
        for (int i = 0; i <= n1; i++) {
            for (int j = 0; j <= n2; j++) {
                if (i != 0 && dp[i - 1][j] && s3.charAt(i + j - 1) == s1.charAt(i - 1))
                    dp[i][j] = true;
                if (j != 0 && dp[i][j - 1] && s3.charAt(i + j - 1) == s2.charAt(j - 1))
                    dp[i][j] = true;
            }
        }
        return dp[n1][n2];

	//Method 2: BFS
        int n1 = s1.length(), n2 = s2.length(), n3 = s3.length();
        if (n1 + n2 != n3) {
            return false;
        }
        HashSet<Integer> visit = new HashSet<Integer>();
        Queue<Integer> queue = new LinkedList<Integer>();
        queue.add(0);
        while (!queue.isEmpty()) {
            int cur = queue.poll();
            int x = cur / (n2 + 1), y = cur % (n2 + 1);
            if (x == n1 && y == n2) {
                return true;
            }
            if (visit.contains(cur)) {
                continue;
            }
            visit.add(cur);
            if (x < n1 && s3.charAt(x + y) == s1.charAt(x))
                queue.offer(cur + n2 + 1);
            if (y < n2 && s3.charAt(x + y) == s2.charAt(y))
                queue.offer(cur + 1);
        }
        return false;

	//Method 3: DFS
        int n1 = s1.length(), n2 = s2.length(), n3 = s3.length();
        if (n1 + n2 != n3) {
            return false;
        }
        HashSet<Integer> visit = new HashSet<Integer>();
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        while (!stack.isEmpty()) {
            int cur = stack.pop();
            int x = cur / (n2 + 1), y = cur % (n2 + 1);
            if (x == n1 && y == n2) {
                return true;
            }
            if (visit.contains(cur)) {
                continue;
            }
            visit.add(cur);
            if (x < n1 && s3.charAt(x + y) == s1.charAt(x))
                stack.push(cur + n2 + 1);
            if (y < n2 && s3.charAt(x + y) == s2.charAt(y))
                stack.push(cur + 1);
        }
        return false;
    }
}
