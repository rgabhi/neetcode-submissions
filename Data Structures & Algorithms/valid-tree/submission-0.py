class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > n - 1:
            return False
        graph = [[] for _ in range(n)]
        q = deque()
        vis = set()
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        q.append((0, -1))
        vis.add(0)
        
        while q:
            u, par = q.popleft()
            for v in graph[u]:
                    if v == par:
                        continue
                    if v not in vis:
                        vis.add(v)
                        q.append((v, u))
        return len(vis) == n
               

        