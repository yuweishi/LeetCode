public class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) {
            return false;
        }
        int[] dict = new int[26];
        for (int i = 0; i < s.length(); i++) {
            dict[s.charAt(i) - 'a']++;
            dict[t.charAt(i) - 'a']--;
        }
        for (int num: dict) {
            if (num != 0)
                return false;
        }
        return true;
    }
}
