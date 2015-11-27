class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n < 3:
            return range(n)
        map = collections.defaultdict(set)
        indegree = [0] * n
        queue = []
        res = []
        #update the indegree of every node
        for edge in edges:
            map[edge[0]].add(edge[1])
            map[edge[1]].add(edge[0])
            indegree[edge[0]] += 1
            indegree[edge[1]] += 1
        #put all nodes with indegree == 1 into queue
        for i in range(n):
            if indegree[i] == 1:
                queue.append(i)
        #topology sort, pop out the nodes with indegree == 1 and push new nodes in layer by layer     
        count = n
        while count > 2:
            newqueue = []
            for current in queue:
                for i in map[current]:
                    indegree[i] -= 1
                    map[i].remove(current)
                    if indegree[i] == 1:
                        newqueue.append(i)
                count -= 1
            queue = newqueue
        return queue
