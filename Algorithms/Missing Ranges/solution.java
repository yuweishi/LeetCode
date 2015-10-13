public class Solution {
    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        List<String> res= new ArrayList<String>();
        int pre = lower;
        for (int num : nums){
            if (pre == num - 1)
                res.add(String.valueOf(pre));
            else if (pre < num - 1)
                res.add(String.valueOf(pre) + "->" + String.valueOf(num - 1));
            pre = num + 1;
        }
        if (pre == upper)
            res.add(String.valueOf(pre));
        else if (pre < upper)
            res.add(String.valueOf(pre) + "->" + String.valueOf(upper));
        return res;
    }
}
