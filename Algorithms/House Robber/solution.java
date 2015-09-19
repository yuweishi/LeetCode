public class Solution {
    public int rob(int[] nums) {
        int robt = 0, robf = 0, temp;
        for (int num: nums) {
            temp = num + robf;
            robf = Math.max(robt, robf);
            robt = temp;
        }
        return Math.max(robt, robf);
    }
}
