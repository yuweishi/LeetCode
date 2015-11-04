public class Solution {
    public void solve(char[][] board) {
        if (board == null || board.length == 0)
            return;
        int m = board.length, n = board[0].length;
        for (int i = 0; i < m; i++) {
            if (board[i][0] == 'O')
                bfs(board, i, 0);
            if (board[i][n - 1] == 'O')
                bfs(board, i, n - 1);
        }
        for (int j = 0; j < n; j++) {
            if (board[0][j] == 'O')
                bfs(board, 0, j);
            if (board[m - 1][j] == 'O')
                bfs(board, m - 1, j);
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (board[i][j] == 'O')
                    board[i][j] = 'X';
                if (board[i][j] == 'N')
                    board[i][j] = 'O';
            }
        }
    }
    public void bfs(char[][] board, int i, int j) {
        Queue<int[]> queue = new LinkedList<>();
        int m = board.length, n = board[0].length;
        queue.offer(new int[]{i, j});
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            i = cur[0]; j = cur[1];
            if (i >= 0 && i < m && j >= 0 && j < n && board[i][j] == 'O') {
                board[i][j] = 'N';
                queue.offer(new int[]{i, j + 1});
                queue.offer(new int[]{i, j - 1});
                queue.offer(new int[]{i + 1, j});
                queue.offer(new int[]{i - 1, j});
            }
        }
    }
}
