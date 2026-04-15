class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = numCourses
        indegree = [0]*n
        graph = [[] for _ in range(n)]

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
           
        q = deque()
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        for deg in indegree:
            if deg > 0:
                return False
        return True
            


