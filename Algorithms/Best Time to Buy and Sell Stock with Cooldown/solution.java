public class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MIN_VALUE, noact = Integer.MIN_VALUE, sell = 0, cooldown = 0;
        for (int price : prices) {
            int pre = sell;
            sell = Math.max(sell, noact + price);
            buy = cooldown - price;
            noact = Math.max(noact, buy);
            cooldown = pre;
        }
        return sell;
    }
}
