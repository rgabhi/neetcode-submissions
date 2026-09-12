class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        vis = set()
        graph={i:[] for i in range(n)}
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(u, parent):
            vis.add(u)
            for v in graph[u]:
                if v == parent:
                    continue
                elif v in vis:
                    return False
                else:
                    dfs(v, u)
            return True

      
        return dfs(0, -1) and len(vis) == n