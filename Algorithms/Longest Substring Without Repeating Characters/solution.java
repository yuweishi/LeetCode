public class Solution {
    public int lengthOfLongestSubstring(String s) {
        HashMap<Character, Integer> dict = new HashMap<>();
        int left = 0;
        int res = 0;
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (dict.containsKey(c) && dict.get(c) >= left) {
                res = Math.max(res, i - left);
                left = dict.get(c) + 1;
            }
            dict.put(c, i);
        }
        return Math.max(res, s.length() - left);
    }
}
