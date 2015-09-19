public class Solution {
    public int rob(int[] nums) {
        if (nums.length == 0) {
            return 0;
        }
        if (nums.length == 1) {
            return nums[0];
        }
        return Math.max(robI(Arrays.copyOfRange(nums, 0, nums.length - 1)), robI(Arrays.copyOfRange(nums, 1, nums.length)));
    }
    public int robI(int[] nums) {
        int robt = 0, robf = 0, temp;
        for (int num: nums) {
            temp = num + robf;
            robf = Math.max(robt, robf);
            robt = temp;
        }
        return Math.max(robt, robf);
    }
}
