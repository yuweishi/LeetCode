public class Solution {
    //Method 1: BFS
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        Queue<Integer> queue = new LinkedList<Integer>();
        int count = 0;
        int[] indegree = new int[numCourses], res = new int[numCourses];
        
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new ArrayList<Integer>());
        }
        
        for (int[] req: prerequisites) {
            map.get(req[1]).add(req[0]);
            indegree[req[0]]++;
        }
        
        for (int i = 0; i < numCourses; i++){
            if (indegree[i] == 0)
                queue.offer(i);
        }
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            res[count] = cur;
            count++;
            for (int next: map.get(cur)) {
                if (--indegree[next] == 0)
                    queue.offer(next);
            }
        }
        
        return count == numCourses ? res : new int[0];
    }

    //Method 2: DFS
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        int[] res = new int[numCourses], visit = new int[numCourses], count = new int[1];
        //initial map with list
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new ArrayList<Integer>());
        }
        
        for (int[] req: prerequisites) {
            map.get(req[0]).add(req[1]);
        }
        
        for (int i = 0; i < numCourses; i++) {
            if (!find(map, i, visit, res, count))
                return new int[0];
        }
        return res;
    }
    private boolean find(Map<Integer, ArrayList<Integer>> map, int cur, int[] visit, int[] res, int[] count) {
        if (visit[cur] == 1)
            return true;
        if (visit[cur] == -1)
            return false;
        visit[cur] = -1;
        for (int pre: map.get(cur)) {
            if (!find(map, pre, visit, res, count))
                return false;
        }
        visit[cur] = 1;
        res[count[0]++] = cur;
        return true;
    }
}
