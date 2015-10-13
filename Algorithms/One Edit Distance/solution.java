public class Solution {
    public boolean isOneEditDistance(String s, String t) {
        int m = s.length(), n = t.length(), i;
        if ((Math.abs(n - m)) > 1)
            return false;
        for (i = 0; i < Math.min(m, n); i++){
            if (s.charAt(i) != t.charAt(i))
                return s.substring(i + (n <= m ? 1: 0)).equals(t.substring(i + (n >= m ? 1: 0)));
        }
        return n != m;
    }
}
