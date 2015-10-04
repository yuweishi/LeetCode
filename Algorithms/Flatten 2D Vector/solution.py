class Vector2D(object):
    #Method 1: Load all elements first
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.list = [num for nums in vec2d for num in nums]

    def next(self):
        """
        :rtype: int
        """
        return self.list.pop(0) if self.list else None

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.list)

    #Method 2: Load one by one
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.row, self.col, self.list = 0, 0, vec2d

    def next(self):
        """
        :rtype: int
        """
        val = self.list[self.row][self.col]
        self.col += 1
        return val

    def hasNext(self):
        """
        :rtype: bool
        """
        while self.row < len(self.list):
            if self.col < len(self.list[self.row]):
                return True
            self.row += 1
            self.col = 0
        return False
