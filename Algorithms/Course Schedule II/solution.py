class Solution(object):
    #Method 1: BFS
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        map = collections.defaultdict(list)
        indegree = [0] * numCourses
        queue = []
        count = 0
        #update the indegree of every node
        for req in prerequisites:
            map[req[1]].append(req[0])
            indegree[req[0]] += 1
        #put all nodes with indegree == 0 into queue
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        #topology sort, always pop out the nodes with indegree == 0, and push new nodes in       
        while count < len(queue):
            current = queue[count]
            for i in map[current]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    queue.append(i)
            count += 1
        return queue if count == numCourses else []

    #Method 2: DFS
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        res = []
        visit = [0] * numCourses
        order = collections.defaultdict(list)
        for req in prerequisites:
            order[req[0]].append(req[1])
        for i in xrange(numCourses):
            if not self.find(order, i, visit, res):
                return []
        return res
    def find(self, order, cur, visit, res):
        if visit[cur] == 1:
            return True
        if visit[cur] == -1:
            return False
        visit[cur] = -1
        for pre in order[cur]:
            if not self.find(order, pre, visit, res):
                return False
        visit[cur] = 1
        res += [cur]
        return True
