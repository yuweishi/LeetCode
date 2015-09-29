public class Solution {
    public int strobogrammaticInRange(String low, String high) {
        int count = 0;
        List<String> res = new ArrayList<String>();
        for(int n = low.length(); n <= high.length(); n++){
            res.addAll(helper(n, n));
        }
        for(String num : res){
            if(!((num.length() == low.length() && num.compareTo(low) < 0) || (num.length() == high.length() && num.compareTo(high) > 0))) count++;
        }
        return count;
    }

    private List<String> helper(int cur, int max){
        if(cur == 0) return new ArrayList<String>(Arrays.asList(""));
        if(cur == 1) return new ArrayList<String>(Arrays.asList("1", "8", "0"));

        List<String> res = new ArrayList<String>();
        List<String> center = helper(cur - 2, max);

        for(int i = 0; i < center.size(); i++){
            String tmp = center.get(i);
            if(cur != max) res.add("0" + tmp + "0");
            res.add("1" + tmp + "1");
            res.add("6" + tmp + "9");
            res.add("8" + tmp + "8");
            res.add("9" + tmp + "6");
        }
        return res;
    }
}
