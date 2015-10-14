public class Solution {
    public int maxProfit(int[] prices) {
        int low = Integer.MAX_VALUE, profit = 0;
        for (int price: prices){
            if (price < low)
                low = price;
            else
                profit = Math.max(profit, price - low);
        }
        return profit;
    }
}
