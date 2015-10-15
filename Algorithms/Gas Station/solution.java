public class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int start = 0, pre = 0, cur = 0, n = gas.length;
        for (int i = 0; i < n; i++){
            cur += gas[i] - cost[i];
            if (cur < 0){
                pre += cur;
                cur = 0;
                start = i + 1;
            }
        }
        return pre + cur >= 0 ? start : -1;
    }
}
