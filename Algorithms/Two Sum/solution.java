public class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> dict = new HashMap<>();
        int[] ans = new int[] {-1, -1};
        for (int i = 0; i < nums.length; i++){
            if (dict.containsKey(nums[i])){
                ans[0] = dict.get(nums[i]);
                ans[1] = i + 1;
                return ans;
            }
            dict.put(target - nums[i], i + 1);
        }
        return ans;
    }
}
