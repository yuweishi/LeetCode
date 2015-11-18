public class Solution {
    public int maxSubArray(int[] nums) {
        if (nums == null || nums.length == 0) {
            return 0;
        }
        int sum = 0;
        int max = nums[0];
        for (int num: nums) {
            sum += num;
            max = Math.max(max, sum);
            sum = Math.max(0, sum);
        }
        return max;
    }
}
