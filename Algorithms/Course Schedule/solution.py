class Solution(object):
    #Method 1: DFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        order = collections.defaultdict(set)
        for req in prerequisites:
            if req[1] in order and self.find(order, req[1], req[0]):
                return False
            order[req[0]].add(req[1])
        return True
    def find(self, order, cur, req):
        if req in order[cur]:
            return True
        for pre in order[cur]:
            if self.find(order, pre, req):
                return True
        return False
