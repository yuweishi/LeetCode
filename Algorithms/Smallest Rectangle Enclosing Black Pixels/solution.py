class Solution(object):
    #Method 1: BFS
    def minArea(self, image, x, y):
        """
        :type image: List[List[str]]
        :type x: int
        :type y: int
        :rtype: int
        """
        x_max, x_min, y_max, y_min = x, x, y, y
        m, n = len(image), len(image[0])
        queue = [(x, y)]
        while queue:
            (i, j) = queue.pop(0)
            if i >= 0 and i < m and j >= 0 and j < n and image[i][j] == '1':
                image[i][j] = '0'
                queue += [(i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j)]
                x_max = max(x_max, i) 
                x_min = min(x_min, i)
                y_max = max(y_max, j)
                y_min = min(y_min, j)
        return (y_max - y_min + 1) * (x_max - x_min + 1)

    #Method 2: Binary Search
    def searchColumns(self, image, i, j, opt):
        while i != j:
            m = (i + j) / 2
            if any([int(row[m]) for row in image]) == opt:
                j = m
            else:
                i = m + 1
        return i
    
    def searchRows(self, image, i, j, opt):
        while i != j:
            m = (i + j) / 2
            if any(map(int, image[m])) == opt:
                j = m
            else:
                i = m + 1
        return i
    
    def minArea(self, image, x, y):
        left = self.searchColumns(image, 0, y, True)
        right = self.searchColumns(image, y + 1, len(image[0]), False)
        top = self.searchRows(image, 0, x, True)
        bottom = self.searchRows(image, x + 1, len(image), False)
        return (right - left) * (bottom - top)
