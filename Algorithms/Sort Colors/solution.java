public class Solution {
    public void sortColors(int[] nums) {
        int index_0 = -1, index_1 = -1, index_2 = -1;
        for (int num: nums){
            nums[++index_2] = 2;
            if (num < 2)
                nums[++index_1] = 1;
            if (num < 1)
                nums[++index_0] = 0;
        }
    }
}
