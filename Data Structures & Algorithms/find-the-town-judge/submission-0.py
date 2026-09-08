class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inedge = [0]*(n+1)
        outedge = [0]*(n+1)
        graph = {}
        for a, b in trust:
            if a not in graph:
                graph[a] = []
            graph[a].append(b)
            inedge[b] += 1
            outedge[a] += 1
        # print(graph)
        for u in range(1, n+1):
            # print(u, inedge[u], outedge[u])
            if inedge[u] == (n-1) and outedge[u] == 0:
                return u
        return -1
       

        