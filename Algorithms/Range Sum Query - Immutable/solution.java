public class NumArray {
    int[] ans;
    public NumArray(int[] nums) {
        ans = new int[nums.length + 1];
        for (int i = 0; i < nums.length; i++) {
            ans[i + 1] = ans[i] + nums[i];
        }
    }

    public int sumRange(int i, int j) {
        return ans[j + 1] - ans[i];
    }
}


// Your NumArray object will be instantiated and called as such:
// NumArray numArray = new NumArray(nums);
// numArray.sumRange(0, 1);
// numArray.sumRange(1, 2);
