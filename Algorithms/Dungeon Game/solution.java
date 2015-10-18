public class Solution {
    public int calculateMinimumHP(int[][] dungeon) {
        if (dungeon == null || dungeon[0].length == 0) return 1;
        int m = dungeon.length, n = dungeon[0].length;
        int[][]ans = new int[m][n];
        for (int i = m - 1; i > -1; i--){
            for (int j = n - 1; j > -1; j--){
                if (j == n - 1 && i == m - 1)
                    ans[i][j] = 1 - dungeon[i][j];
                else if (j == n - 1)
                    ans[i][j] = ans[i + 1][j] - dungeon[i][j];
                else if (i == m - 1)
                    ans[i][j] = ans[i][j + 1] - dungeon[i][j];
                else
                    ans[i][j] = Math.min(ans[i + 1][j], ans[i][j + 1]) - dungeon[i][j];
                ans[i][j] = Math.max(1, ans[i][j]);
            }
        }
        return ans[0][0];
    }
}
