public class Solution {
    public int nthUglyNumber(int n) {
        int index2 = 0, index3 = 0, index5 = 0, u2 = 2, u3 = 3, u5 = 5, i;
        int [] ugly = new int [n];
        ugly[0] = 1;
        for (i = 1; i < n; i ++){
            ugly[i] = Math.min(Math.min(u2, u3), u5);
            if (ugly[i] == u2){
                u2 = 2 * ugly[++index2];
            }
            if (ugly[i] == u3){
                u3 = 3 * ugly[++index3];
            }
            if (ugly[i] == u5){
                u5 = 5 * ugly[++index5];
            }
        }
        return ugly[n - 1];
    }
}
