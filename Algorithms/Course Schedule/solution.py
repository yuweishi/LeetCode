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

    #Method 2: BFS
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        map = collections.defaultdict(list)
        indegree = [0] * numCourses
        queue = []
        count = numCourses
        #update the indegree of every node
        for req in prerequisites:
            map[req[0]].append(req[1])
            indegree[req[1]] += 1
        #put all nodes with indegree == 0 into queue
        for i in range(count):
            if indegree[i] == 0:
                queue.append(i)
        #topology sort, always pop out the nodes with indegree == 0, and push new nodes in       
        while queue:
            current = queue.pop(0)
            for i in map[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            count -= 1
        return count == 0
