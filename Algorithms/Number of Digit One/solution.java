public class Solution {
    public int countDigitOne(int n) {
        int ones = 0;
        for (long base = 1; base <= n; base *= 10){
            long left = n / 10 / base, cur = (n / base) % 10, right = n % base;
            ones += left * base;
            if (cur > 1) {
                ones += base;
            }
            else if (cur == 1) {
                ones += right + 1;
            }
        }
        return ones;
    }
}
