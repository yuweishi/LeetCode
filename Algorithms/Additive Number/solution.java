public class Solution {
    public boolean isAdditiveNumber(String num) {
        if (num == null || num.length() < 3) {
            return false;
        }
        int n = num.length();
        for (int i = 1; i <= n / 2; i++) {
            for (int j = i + 1; j <= i + (n - i) / 2; j++) {
                int start1 = 0, start2 = i, start3 = j;
                while (start3 < n) {
                    Long cur = (Long.parseLong(num.substring(start1, start2)) + Long.parseLong(num.substring(start2, start3)));
                    if (num.substring(start3).startsWith(cur.toString())) {
                        start1 = start2;
                        start2 = start3;
                        start3 += cur.toString().length();
                    }
                    else {
                        break;
                    }
                }
                if (start3 == n) {
                    return true;
                }
                if (num.charAt(i) == '0') {
                    break;
                }
            }
            if (num.charAt(0) == '0') {
                break;
            }
        }
        return false;
    }
}
