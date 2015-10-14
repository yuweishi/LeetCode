public class Solution {
    public int maxProfit(int k, int[] prices) {
        if (k == 0 || prices == null || prices.length == 0) return 0;
        if (k > prices.length / 2){
            int profit = 0;
            for (int i = 1; i < prices.length; i++){
                if (prices[i] > prices[i - 1]) profit += prices[i] - prices[i - 1];
            }
            return profit;
        }
        int[] buy = new int[k], sell = new int[k];
        for (int i = 0; i < k; i++) buy[i] = Integer.MIN_VALUE;
        for (int price : prices){
            for (int i = k - 1; i > 0; i--){
                sell[i] = Math.max(sell[i], price + buy[i]);
                buy[i] = Math.max(buy[i], sell[i - 1] - price);
            }
            sell[0] = Math.max(sell[0], price + buy[0]);
            buy[0] = Math.max(buy[0], -price);
        }
        return sell[k - 1];
    }
}
