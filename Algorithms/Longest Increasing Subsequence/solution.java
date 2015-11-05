public class Solution {
    public int lengthOfLIS(int[] nums) {
        //Method 1: DP
        if (nums == null) 
            return 0;
        if (nums.length < 2)
            return nums.length;
        int res = 0;
        int[] dp = new int[nums.length];
        for (int i = 0; i < nums.length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] > nums[j])
                    dp[i] = Math.max(dp[i], dp[j] + 1);
            }
            res = Math.max(res, dp[i]);
        }
        return res + 1;

	//Method 2: Binary Seaech
        if (nums == null) 
            return 0;
        int len = 0;
        int[] dp = new int[nums.length];
        for(int x : nums) {
            int i = Arrays.binarySearch(dp, 0, len, x);
            if (i < 0) 
                i = -(i + 1);
            dp[i] = x;
            if (i == len) 
                len++;
        }
        return len;
    }
}
