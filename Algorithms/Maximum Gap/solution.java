public class Solution {
    public int maximumGap(int[] num) {
        if (num == null || num.length < 2) {
            return 0;
        }
        int n = num.length;
        int min = num[0];
        int max = num[0];
        for (int number : num) {
            min = Math.min(min, number);
            max = Math.max(max, number);
        }
        int gap = (int)Math.ceil((double)(max - min) / (n - 1));
        if (gap == 0) {
            return 0;
        }
        int[] bucket_min = new int[n]; Arrays.fill(bucket_min, Integer.MAX_VALUE);
        int[] bucket_max = new int[n]; Arrays.fill(bucket_max, Integer.MIN_VALUE);
        for (int number: num) {
            int i = (number - min) / gap;
            bucket_min[i] = Math.min(bucket_min[i], number);
            bucket_max[i] = Math.max(bucket_max[i], number);
        }
        int res = 0;
        int pre = min;
        for (int i = 0; i < n; i++) {
            if (bucket_min[i] != Integer.MAX_VALUE) {
                res = Math.max(res, bucket_min[i] - pre);
                pre = bucket_max[i];
            }
        }
        return res;
    }
}
