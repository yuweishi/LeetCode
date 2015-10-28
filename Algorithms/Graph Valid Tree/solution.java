public class Solution {
    public boolean validTree(int n, int[][] edges) {
        if (n != edges.length + 1)
            return false;
        int [] root = new int[n];
        Arrays.fill(root, -1);
        for (int[] edge: edges){
            int x = find(root, edge[0]);
            int y = find(root, edge[1]);
            if (x == y)
                return false;
            root[x] = y;
        }
        return true;
    }
    
    public int find(int[] root, int i){
        if (root[i] == -1)
            return i;
        return find(root, root[i]);
    }
}
