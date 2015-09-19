public class Solution {
    public void moveZeroes(int[] nums) {
        int right, n = nums.length;
        for (int left = 0; left < n - 1; left++) {
            if (nums[left] == 0) {
                right = left + 1;
                while (nums[right] == 0) {
                    right++;
                    if (right == n) return;
                }
                int temp = nums[left];
                nums[left] = nums[right];
                nums[right] = temp;
            }
        }
    }
}
