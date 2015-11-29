public class Solution {
    //Method 1: DP
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) return false;
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int i = 0; i < n; i++) {
            if (p.charAt(i) == '*') {
                if (i == 0 || p.charAt(i - 1) == '*') {
                    return false;
                }
                dp[0][i + 1] = dp[0][i - 1];
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] && (p.charAt(j) == '.' || p.charAt(j) == s.charAt(i)))
                    dp[i + 1][j + 1] = true;
                if (p.charAt(j) == '*' && (dp[i + 1][j - 1] || dp[i][j + 1] && (p.charAt(j - 1) == '.' || p.charAt(j - 1) == s.charAt(i))))
                    dp[i + 1][j + 1] = true;
            }
        }
        return dp[m][n];
    }
}
