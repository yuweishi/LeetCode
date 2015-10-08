public class Solution {
    public boolean wordPattern(String pattern, String str) {
        String [] s = str.split(" ");
        if (s.length != pattern.length()) return false;
        Map dict = new HashMap();
        for (int i = 0; i < s.length; ++i){
            if (!Objects.equals(dict.put(pattern.charAt(i), i), dict.put(s[i], i)))    return false;
        }
        return true;
    }
}
