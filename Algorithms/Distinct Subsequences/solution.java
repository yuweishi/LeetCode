public class Solution {
    public int numDistinct(String s, String t) {
        if (s.length() < t.length()) 
            return 0;
        int[] dp = new int[s.length() + 1];
        Arrays.fill(dp, 1);
        for (int i = 0; i < t.length(); i++) {
            int pre = 0;
            for (int j = 0; j < s.length(); j++) {
                int cur = pre + (s.charAt(j) == t.charAt(i) ? dp[j]: 0);
                dp[j] = pre;
                pre = cur;
            }
            dp[s.length()] = pre;
        }
        return dp[dp.length - 1];
    }
}
