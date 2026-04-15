class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        cnt = 0
        graph = {i : [] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        vis = set()
        def dfs(i):
            for v in graph[i]:
                if v not in vis:
                    vis.add(v)
                    dfs(v)
        
        for i in range(n):
            if not i in vis:
                vis.add(i)
                dfs(i)
                cnt += 1
        return cnt

            