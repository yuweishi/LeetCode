public class Solution {
    public String largestNumber(int[] nums) {
        String[] strs = new String[nums.length];
        for (int i = 0; i < nums.length; i++) {
            strs[i] = "" + nums[i];
        }
        
        Comparator<String> comp = new Comparator<String>(){
            @Override
            public int compare(String str1, String str2){
                String s1 = str1 + str2;
                String s2 = str2 + str1;
                return s2.compareTo(s1);
            }
        };
        Arrays.sort(strs, comp);
        
        String res = "";
        for (String str: strs) {
            if (res.length() > 0 || !str.equals("0"))
                res += str;
        }
        return res.length() == 0? "0" : res;
    }
}
