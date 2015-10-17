public class Solution {
    public String longestPalindrome(String s) {
        String str = preProcess(s);
        int id = 0, mx = 0, n = str.length();
        int[] p = new int[n];
        for (int i = 1; i < n - 1; i++) {
            p[i] = mx > i ? Math.min(p[2 * id - i], mx - i) : 0;
            while (str.charAt(i + 1 + p[i]) == str.charAt(i - 1 - p[i]))
                p[i]++;
            if (i + p[i] > mx) {
                mx = i + p[i];
                id = i;
            }
        }

        int maxLen = 0, center = 0;
        for (int i = 1; i < n - 1; i++) {
            if (p[i] > maxLen) {
                maxLen = p[i];
                center = i;
            }
        }
        int pos = (center - 1 - maxLen) / 2;
        return s.substring(pos, pos + maxLen);
    }

    private String preProcess(String s) {
       StringBuffer sb = new StringBuffer("^");
       for (int i = 0; i < s.length(); i++)
          sb.append("#").append(s.charAt(i));
       sb.append("#$");
       return sb.toString();
    }
}
