public class Solution {
    public int maxProfit(int[] prices) {
        int[] ans = check(prices);
        int profit1 = ans[0], low = ans[1], high = ans[2];
        int[] ans1 = check(Arrays.copyOfRange(prices, 0, low)), ans2 = check(Arrays.copyOfRange(prices, high, prices.length));
        int profit2 = Math.max(ans1[0], ans2[0]);
        for (int i = low; i < high; i++) prices[i] = -prices[i];
        int[] ans3 = (profit1 > 0) ? check(Arrays.copyOfRange(prices, low, high)) : new int[] {0};
        return profit1 + Math.max(profit2, ans3[0]);
    }
    
    private int[] check(int[] prices){
        int low_temp = 0, low = 0, high = prices.length - 1, profit = 0, dif, i;
        for (i = 0; i < prices.length; i++){
            dif = prices[i] - prices[low_temp];
            if (dif < 0)
                low_temp = i;
            else if (dif > profit){
                low = low_temp;
                high = i;
                profit = dif;
            }
        }
        return new int[] {profit, low, high + 1};
    }
}
