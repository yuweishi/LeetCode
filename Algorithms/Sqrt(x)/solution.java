public class Solution {
    public int mySqrt(int x) {
        if (x < 2){
            return x;
        }
        int start = 1, end = x, mid;
        while (end - start > 1){
            //if use (end + start) / 2, overflow
            mid = start + (end - start) / 2;
            //if use (mid * mid > x), overflow
            if (mid > x / mid){
                end = mid;
            }
            else if (mid < x / mid){
                start = mid;
            }
            else{
                return mid;
            }
        }
        return start;
    }
}
