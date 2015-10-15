public class Solution {
    public int candy(int[] ratings) {
        if (ratings == null || ratings.length == 0) return 0;
        int down = 0, up = 1, sum = 1;
        for (int i = 1; i < ratings.length; i++){
            if (ratings[i] >= ratings[i - 1]){
                if (down > 0){
                    sum += (down + 1) * down / 2;
                    if (down >= up) sum += (down + 1) - up;
                    down = 0;
                    up = 1;
                }
                up = ratings[i] == ratings[i - 1] ? 1: up + 1;
                sum += up;
            }
            else down++;
        }
        if (down > 0){
            sum += (down + 1) * down / 2;
            if (down >= up) sum += (down + 1) - up;
        }
        return sum;
    }
}
