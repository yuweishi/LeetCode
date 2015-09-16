public class Solution {
    public int titleToNumber(String s) {
        int res = 0, i = 0, n = s.length();
        while (i < n){
            res = res * 26 + s.charAt(i) - 'A' + 1;
            i ++;
        }
        return res;
    }
}
