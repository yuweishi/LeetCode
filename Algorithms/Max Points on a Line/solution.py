# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxi = 0
        for i in range(len(points)):
            same = 1
            x1, y1 = points[i].x, points[i].y
            dict = {'inf': 0}
            for j in range(i + 1, len(points)):
                x2, y2 = points[j].x, points[j].y
                if x1 == x2 and y1 == y2:
                    same += 1
                    continue
                if x1 == x2:
                    key = 'inf'
                else:
                    key = float((y1- y2)) / (x1 - x2)
                dict[key] = dict[key] + 1 if key in dict else 1
            maxi = max(maxi, same + max(dict.values()))
        return maxi
