public class Solution {
    //Method 1: iterative to avoid stack overflow
    public double myPow(double x, int n) {
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        double pow = 1;
        while (n > 0) {
            if ((n & 1) == 1) {
                pow = pow * x;
            }
            x *= x;
            n >>= 1;
        }
        return pow;
    }
    //Method 2: recursive, may overflow
    public double myPow(double x, int n) {
        if (n == 0) {
            return 1;
        }
        if (n < 0) {
            x = 1 / x;
            n = -n;
        }
        if (n % 2 == 1){
            return x * myPow(x, n - 1);
        }
        double temp = myPow(x, n / 2);
        return temp * temp;
    }
}
