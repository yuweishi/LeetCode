public class Solution {
    #Method 1: go through twice
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

    #Method 2: DP
    public int maxProfit(int[] prices) {
        int buy1 = Integer.MAX_VALUE, buy2 = Integer.MAX_VALUE, sell1 = 0, sell2 = 0;
        for(int price: prices){                      // Assume we only have 0 money at first
            sell2 = Math.max(sell2, price - buy2);   // The maximum if we've just sold 2nd stock so far.
            buy2  = Math.min(buy2,  price - sell1);  // The maximum if we've just buy  2nd stock so far.
            sell1 = Math.max(sell1, price - buy1);   // The maximum if we've just sold 1nd stock so far.
            buy1  = Math.min(buy1,  price);          // The maximum if we've just buy  1st stock so far. 
        }
        return sell2; ///Since release1 is initiated as 0, so release2 will always higher than release1.
    }
}
