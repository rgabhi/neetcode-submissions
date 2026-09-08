"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone = {}
        clone[node] = Node(node.val)
        q = deque([node])
        while q:
            u = q.popleft()
            for v in u.neighbors:
                if v not in clone:
                    q.append(v)
                    clone[v] = Node(v.val)
                clone[u].neighbors.append(clone[v])
        return clone[node]


        



        