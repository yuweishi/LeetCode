public class Solution {
    public int divide(int dividend, int divisor) {
        if (divisor == 0 || dividend == -2147483648 && divisor == -1)
            return 2147483647;
        int res = 0, sign = (dividend > 0 && divisor < 0 || dividend < 0 && divisor > 0) ? -1 : 1;
        if (dividend > 0) dividend = -dividend;
        if (divisor > 0) divisor = -divisor;
        while (divisor >= dividend) {
            int temp = divisor, base = 1;
            while (temp >= dividend) {
                res += base;
                base <<= 1;
                dividend -= temp;
                if (temp > -2147483648 >> 1)
                    temp <<= 1;
            }
        }
        return sign * res;
    }
}
