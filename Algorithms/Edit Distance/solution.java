public class Solution {
    public int minDistance(String word1, String word2) {
        int len1 = word1.length();
        int len2 = word2.length();
        int pre, cur;
        int[] dp = new int[len2 + 1];
        for (int i = 0; i <= len2; i++)
            dp[i] = i;
        for (int i = 0; i < len1; i++) {
            pre = i + 1;
            for (int j = 0; j < len2; j++) {
                if (word1.charAt(i) != word2.charAt(j)) 
                    cur = 1 + Math.min(pre, Math.min(dp[j], dp[j + 1]));
                else
                    cur = dp[j];
                dp[j] = pre;
                pre = cur;
            }
            dp[len2] = pre;
        }
        return dp[len2];
    }
}
