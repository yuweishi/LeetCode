public class Solution {
    //Method 1: DP
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) return false;
        int m = s.length(), n = p.length();
        boolean[][] dp = new boolean[m + 1][n + 1];
        dp[0][0] = true;
        for (int i = 0; i < n; i++) {
            if (p.charAt(i) == '*') {
                dp[0][i + 1] = dp[0][i];
            }
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (dp[i][j] && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i)))
                    dp[i + 1][j + 1] = true;
                if (p.charAt(j) == '*' && (dp[i][j + 1] || dp[i + 1][j] || dp[i][j]))
                    dp[i + 1][j + 1] = true;
            }
        }
        return dp[m][n];
    }

    //Method 2: Greedy
    public boolean isMatch(String s, String p) {
        if (s == null || p == null) return false;
        int m = s.length(), n = p.length(), star = -1, i_pre = -1, i = 0, j = 0;
        while (i < m) {
            if (j < n && (p.charAt(j) == '?' || p.charAt(j) == s.charAt(i))) {
                i++;
                j++;
            }
            else if (j < n && p.charAt(j) == '*') {
                i_pre = i;
                star = ++j;
            }
            else if (star != -1) {
                i = ++i_pre;
                j = star;
            }
            else
                return false;
        }
        while (j < n && p.charAt(j) == '*') {
            j++;
        }
        return j == n;
    }
}
