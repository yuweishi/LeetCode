class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        if not rooms: return
        m, n = len(rooms), len(rooms[0])
        stack = [(x, y) for x in xrange(m) for y in xrange(n) if rooms[x][y] == 0]
        while stack:
            (x, y) = stack.pop(0)
            cur = rooms[x][y]
            for (i, j) in [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]:
                if (i >= 0 and i < m and j >= 0 and j < n and rooms[i][j] == 2147483647):
                    rooms[i][j] = cur + 1
                    stack.append((i, j))
        
