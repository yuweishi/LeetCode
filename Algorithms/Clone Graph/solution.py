# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        self.dict = {}
        if node == None: 
            return None
        return self.clone(node)
    def clone(self, node):
        if node.label in self.dict:
            return self.dict[node.label]
        new = UndirectedGraphNode(node.label)
        self.dict[new.label] = new
        for neighbor in node.neighbors:
            new.neighbors.append(self.clone(neighbor))
        return new
