class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        n = numCourses
        graph = {i : [] for i in range(n)}
        indegree = [0]*n
        ans = []
        q = deque()
        cnt = 0

        for u, v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        
        for i in range(n):
            if indegree[i] == 0:
                q.append(i)
        
        while q:
            u = q.popleft()
            ans.append(u)
            cnt += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        
        if cnt != n:
            return []
        return ans

        

        