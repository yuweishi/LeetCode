public class Solution {
    public int lengthOfLongestSubstringTwoDistinct(String s) {
        if (s == null) return 0;
        int start1 = -1, start2 = -1, res = 0;
        for (int i = 1; i < s.length(); i++) {
            if (s.charAt(i) == s.charAt(i - 1))
                continue;
            if (start2 < 0 || s.charAt(start2) == s.charAt(i)) {
                start2 = i - 1;
            }
            else {
                res = Math.max(res, i - start1 - 1);
                start1 = start2;
                start2 = i - 1;
            }
        }
        return Math.max(res, s.length() - start1 - 1);
    }
}
