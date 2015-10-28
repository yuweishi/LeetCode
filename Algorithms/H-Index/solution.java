public class Solution {
    public int hIndex(int[] citations) {
        int count = 0, n = citations.length;
        int [] arr = new int [n + 1];
        for (int num: citations){
            if (num >= n)
                arr[n] += 1;
            else
                arr[num] += 1;
        }
        
        for (int i = n; i >= 0; i--){
            count += arr[i];
            if (count >= i)
                return i;
        }
        return 0;
    }
}
