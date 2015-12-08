public class Solution {
    public int maxCoins(int[] nums) {
        int[] nums_new = new int[nums.length + 2];
        int n = 1;
        for (int num: nums) {
            if (num > 0) {
                nums_new[n++] = num;
            }
        }
        nums_new[0] = nums_new[n++] = 1;
        int[][] dp = new int[n][n];
        
        for (int len = 2; len < n; len++) {
            for (int left = 0; left < n - len; left++) {
                int right = left + len;
                for (int i = left + 1; i < right; i++) {
                    dp[left][right] = Math.max(dp[left][right], nums_new[left] * nums_new[i] * nums_new[right] + dp[left][i] + dp[i][right]);
                }
            }
        }
        return dp[0][n - 1];
    }
}
