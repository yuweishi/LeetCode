public class Solution {
    public boolean containsNearbyAlmostDuplicate(int[] nums, int k, int t) {
        if (k < 1 || t < 0) return false;
        HashMap<Integer, Long> dict = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int cur_key = nums[i] / (t + 1);
            for (int key = cur_key - 1; key <= cur_key + 1; key++) {
                if (dict.containsKey(key) && Math.abs((long)dict.get(key) - nums[i]) <= t)
                    return true;
            }
            if (i + 1 > k) {
                dict.remove(nums[i - k] / (t + 1));
            }
            dict.put(cur_key, (long) nums[i]);
        }
        return false;
    }
}
