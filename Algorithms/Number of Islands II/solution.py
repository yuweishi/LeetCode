class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        parent, rank, count = {}, {}, [0]
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if rank[x] < rank[y]:
                    x, y = y, x
                parent[y] = x
                rank[x] += rank[x] == rank[y]
                count[0] -= 1
        def add((i, j)):
            x = parent[x] = i, j
            rank[x] = 0
            count[0] += 1
            for y in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if y in parent:
                    union(x, y)
            return count[0]
        return map(add, positions)
