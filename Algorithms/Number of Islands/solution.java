public class Solution {
    //Method 1: BFS
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    Queue<int[]> queue = new LinkedList<>();
                    queue.offer(new int[] {i, j});
                    bfs(grid, queue);
                    count++;
                }
            }
        }
        return count;
    }
    
    private void bfs(char[][] grid, Queue<int[]> queue) {
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            int x = cur[0], y = cur[1];
            if (x < grid.length && x >= 0 && y < grid[0].length && y >= 0 && grid[x][y] == '1') {
                grid[x][y] = '0';
                queue.add(new int[] {x, y + 1});
                queue.add(new int[] {x, y - 1});
                queue.add(new int[] {x + 1, y});
                queue.add(new int[] {x - 1, y});
            }
        }
    }

    //Method 2: DFS
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0)
            return 0;
        int count = 0;
        for (int i = 0; i < grid.length; i++) {
            for (int j = 0; j < grid[0].length; j++) {
                if (grid[i][j] == '1') {
                    dfs(grid, i, j);
                    count++;
                }
            }
        }
        return count;
    }
    
    private void dfs(char[][] grid, int x, int y) {
        if (x < grid.length && x >= 0 && y < grid[0].length && y >= 0 && grid[x][y] == '1') {
            grid[x][y] = '0';
            dfs(grid, x, y + 1);
            dfs(grid, x, y - 1);
            dfs(grid, x + 1, y);
            dfs(grid, x - 1, y);
        }
    }
}
