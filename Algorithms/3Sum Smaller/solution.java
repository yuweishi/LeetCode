public class Solution {
    public int threeSumSmaller(int[] nums, int target) {
        int res = 0, n = nums.length, i, j, k;
        Arrays.sort(nums);
        for (i = 0; i < n - 2; i++) {
            j = i + 1; k = n - 1;
            while (j < k) {
                if (nums[i] + nums[j] + nums[k] >= target) k -= 1;
                else {
                    res += k - j;
                    j++;
                }
            }
        }
        return res;
    }
}
