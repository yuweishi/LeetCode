public class Solution {
    public int maximalSquare(char[][] matrix) {
        if (matrix == null || matrix.length == 0)
            return 0;
        int pre = 0, max = 0;
        int[] dp = new int[matrix[0].length + 1];
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[0].length; j++) {
                int temp = dp[j + 1];
                if (matrix[i][j] == '1') {
                    dp[j + 1] = 1 + Math.min(pre, Math.min(dp[j], dp[j + 1]));
                    max = Math.max(max, dp[j + 1]);
                }
                else
                    dp[j + 1] = 0;
                pre = temp;
            }
        }
        return max * max;
    }
}
