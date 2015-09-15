public class Solution {
    public boolean isHappy(int n) {
        int slow = check(n), fast = check(check(n));
        while (fast != 1 && slow != fast){
            slow = check(slow);
            fast = check(check(fast));
        }
        return fast == 1;
    }
    public int check(int n){
        int sum = 0;
        while (n > 0){
            sum += (n % 10) * (n % 10);
            n /= 10;
        }
        return sum;
    }
}
