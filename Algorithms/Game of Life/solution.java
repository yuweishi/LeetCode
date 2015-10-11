public class Solution {
    public void gameOfLife(int[][] board) {
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                int count = 0;
                for (int p = Math.max(0, i - 1); p < Math.min(m, i + 2); p++){
                    for (int q = Math.max(0, j - 1); q < Math.min(n, j + 2); q++){
                        count += board[p][q] % 2;
                    }
                }
                if (count == 3 || count - board[i][j] == 3)
                    board[i][j] |= 2;
            }
        }
        for (int i = 0; i < m; i++){
            for (int j = 0; j < n; j++){
                board[i][j] >>= 1;
            }
        }
    }
}
