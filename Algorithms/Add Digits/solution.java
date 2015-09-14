public class Solution {
    public int addDigits(int num) {
        int res = num % 9;
        return (num != 0 && res == 0) ? 9 : res;
    }
}
