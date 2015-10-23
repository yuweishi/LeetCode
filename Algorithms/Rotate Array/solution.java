public class Solution {
    public void rotate(int[] nums, int k) {
        int len = nums.length, n = nums.length, bias = 0, temp;
        k = k % n;
        while (k > 0){
            for (int i = 0; i < k; i++){
                temp = nums[len - k + i];
                nums[len - k + i] = nums[bias + i];
                nums[bias + i] = temp;
            }
            bias += k;
            n -= k;
            k %= n;
        }
    }
}
