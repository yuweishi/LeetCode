public class Solution {
    public List<Integer> numIslands2(int m, int n, int[][] positions) {
        List<Integer> res = new ArrayList<Integer>();
        HashMap<Integer, Integer> parent = new HashMap<Integer, Integer>();
        HashMap<Integer, Integer> rank = new HashMap<Integer, Integer>();
        int[] base_x = new int[] {0, 0, -1, 1};
        int[] base_y = new int[] {-1, 1, 0, 0};
        int[] count = new int[1];
        for (int i = 0; i < positions.length; i++) {
            int x = positions[i][0];
            int y = positions[i][1];
            int cur = x * n + y;
            rank.put(cur, 0);
            parent.put(cur, cur);
            count[0]++;
            for (int j = 0; j < 4; j++) {
                int x1 = x + base_x[j];
                int y1 = y + base_y[j];
                if (x1 >= 0  && x1 < m && y1 >= 0 && y1 < n) {
                    int neighbor = x1 * n + y1;
                    if (parent.containsKey(neighbor)) {
                        union(cur, neighbor, parent, rank, count);
                    }
                }
            }
            res.add(count[0]);
        }
        return res;
    }
    public int find(int x, HashMap<Integer, Integer> parent) {
        if (parent.get(x) != x) {
            parent.put(x, find(parent.get(x), parent));
        }
        return parent.get(x);
    }
    public void union(int x, int y, HashMap<Integer, Integer> parent, HashMap<Integer, Integer> rank, int[] count) {
        x = find(x, parent);
        y = find(y, parent);
        if (x != y) {
            if (rank.get(x) < rank.get(y)) {
                x = x + y;
                y = x - y;
                x = x - y;
            }
            parent.put(y, x);
            rank.put(x, rank.get(x) + (rank.get(x) == rank.get(y) ? 1: 0));
            count[0]--;
        }
    }
}
