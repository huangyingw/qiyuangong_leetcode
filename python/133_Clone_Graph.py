# Definition for a undirected graph node
# class UndirectedGraphNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution(object):

    def __init__(self):
        self.label_map = {}

    def cloneGraph(self, node):
        """
        :type node: UndirectedGraphNode
        :rtype: UndirectedGraphNode
        """
        if node is None:
            return None
        res = UndirectedGraphNode(node.label)
        self.label_map[node.label] = res
        for ne in node.neighbors:
            if ne.label not in self.label_map:
                res.neighbors.append(self.cloneGraph(ne))
            else:
                res.neighbors.append(self.label_map[ne.label])
        return res
