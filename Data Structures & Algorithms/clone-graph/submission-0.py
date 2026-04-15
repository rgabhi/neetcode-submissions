"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    hm = {}
    vis = set()

    def bfs_1(self, node: Optional['Node']) -> None:
        if node is None:
            return
        q = deque()
        q.append(node)
        self.vis.add(node.val)
        while q:
            tmp = q.popleft()
            self.hm[tmp.val] = Node(tmp.val)
            for neighbor in tmp.neighbors:
                if neighbor.val not in self.vis:
                    q.append(neighbor)
                    self.vis.add(neighbor.val)

    def bfs_2(self, node : Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        q = deque()
        q.append(node)
        new_node = self.hm[node.val]
        self.vis.remove(node.val)
        while q:
            tmp = q.popleft()
            curr_node = self.hm[tmp.val]
            for neighbor in tmp.neighbors:
                curr_node.neighbors.append(self.hm[neighbor.val])
                if neighbor.val in self.vis:
                    q.append(neighbor)
                    self.vis.remove(neighbor.val)
        return new_node
                

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        self.bfs_1(node)
        # print(self.vis)
        return self.bfs_2(node)

        