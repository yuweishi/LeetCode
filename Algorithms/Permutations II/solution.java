public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        List<List<Integer>> res = new ArrayList<>();
        if (nums == null || nums.length == 0) return res;
        res.add(new ArrayList<>());
        for (int i = 0; i < nums.length; i++){
            List<List<Integer>> newres = new ArrayList<>();
            for (List<Integer> l : res){            
                for (int j = 0; j <= i; j++){
                    #only insert before the position of same value
		    if (j > 0 && l.get(j - 1) == nums[i])
                        break;
                    List<Integer> new_l = new ArrayList<Integer>(l);
                    new_l.add(j, nums[i]);
                    newres.add(new_l);
                }
            }
            res = newres;
        }
        return res;
    }
}
