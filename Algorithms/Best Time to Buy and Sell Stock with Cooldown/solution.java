public class Solution {
    public int maxProfit(int[] prices) {
        int buy = Integer.MIN_VALUE, buy_pre = Integer.MIN_VALUE, sell = 0, sell_pre = 0;
        for (int price : prices) {
            buy_pre = buy;
            buy = Math.max(buy, sell_pre - price);
            sell_pre = sell;
            sell = Math.max(sell, buy_pre + price);
        }
        return sell;
    }
}
