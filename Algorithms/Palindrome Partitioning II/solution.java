public class Solution {
    //Method 1: time complexity O(n2), space complexity O(n2)
    public int minCut(String s) { 
        int n = s.length();
        int[] dp = new int[n + 1]; dp[0] = -1;
        boolean[][] pal = new boolean[n + 1][n + 1];
        for (int end = 1; end < n; end++){
            dp[end + 1] = end;
            for (int start = end; start >= 0; start--){
                if (s.charAt(start) == s.charAt(end) && (end - start <= 2 || pal[start + 1][end - 1])){
                    pal[start][end] = true;
                    dp[end + 1] = Math.min(dp[end + 1], 1 + dp[start]);
                }
            }
        }
        return dp[n];
    }

   //Method 2: time complexity O(n2), space complexity O(n2) 
    public int minCut(String s) {
        int n = s.length();
        int[] dp = new int[n + 1]; 
        for (int i = 0; i <= n; i++) dp[i] = i - 1;
        for (int center = 0; center < n; center++){
            for (int size = 0; center - size >= 0 && center + size < n && s.charAt(center + size) == s.charAt(center - size); size++)
                dp[center + size + 1] = Math.min(dp[center + size + 1], 1 + dp[center - size]);
            for (int size = 1; center - size + 1>= 0 && center + size < n && s.charAt(center + size) == s.charAt(center - size + 1); size++)
                dp[center + size + 1] = Math.min(dp[center + size + 1], 1 + dp[center - size + 1]);
        }
        return dp[n];
    }
}
