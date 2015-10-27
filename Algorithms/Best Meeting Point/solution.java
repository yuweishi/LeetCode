public class Solution {
    public int minTotalDistance(int[][] grid) {
        List<Integer> col = new ArrayList<Integer>(), row = new ArrayList<Integer>();
        for (int i = 0; i < grid.length; i ++){
            for (int j = 0; j < grid[0].length; j++){
                if (grid[i][j] == 1){
                    row.add(i);
                    col.add(j);
                }
            }
        }
        
        Collections.sort(col);
        int res = 0, left = 0, right = row.size() - 1;
        while (left < right)
            res += col.get(right) - col.get(left) + row.get(right--) - row.get(left++);
        return res;
    }
}
