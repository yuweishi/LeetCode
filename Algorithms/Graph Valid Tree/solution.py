class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if len(edges) != n - 1:
            return False
        graph = range(n)
        for edge in edges:
            x = self.find(graph, edge[0])
            y = self.find(graph, edge[1])
            if x == y:
                return False
            graph[x] = y
        return True
        
    def find(self, graph, i):
        if graph[i] == i: return i
        return self.find(graph, graph[i])
