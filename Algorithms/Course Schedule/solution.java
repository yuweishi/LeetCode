public class Solution {
    //Method 1: BFS
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, ArrayList<Integer>> map = new HashMap<>();
        Queue<Integer> queue = new LinkedList<Integer>();
        int count = numCourses;
        int[] indegree = new int[count];
        
        for (int i = 0; i < count; i++) {
            map.put(i, new ArrayList<Integer>());
        }
        
        for (int[] req: prerequisites) {
            map.get(req[1]).add(req[0]);
            indegree[req[0]]++;
        }
        
        for (int i = 0; i < count; i++){
            if (indegree[i] == 0)
                queue.offer(i);
        }
        
        while(!queue.isEmpty()) {
            int cur = queue.poll();
            count--;
            for (int next: map.get(cur)) {
                if (--indegree[next] == 0)
                    queue.offer(next);
            }
        }
        
        return count == 0;
    }

    //Method 2: DFS
    //Method 2: DFS
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        Map<Integer, HashSet<Integer>> map = new HashMap<>();
        //initial map with hashset
        for (int i = 0; i < numCourses; i++) {
            map.put(i, new HashSet<Integer>());
        }
        
        for (int[] req: prerequisites) {
            //if req[0] is prerequisites of req[1], return false
            if (find(map, req[1], req[0]))
                return false;
            map.get(req[0]).add(req[1]);
        }
        return true;
    }
    private boolean find(Map<Integer, HashSet<Integer>> map, int cur, int req) {
        if (map.get(cur).contains(req))
            return true;
        for (int pre: map.get(cur)) {
            if (find(map, pre, req))
                return true;
        }
        return false;
    }
}
