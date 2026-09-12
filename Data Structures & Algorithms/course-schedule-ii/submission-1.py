class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        q = deque()
        indegree = [0]*numCourses
        graph = {i: [] for i in range(numCourses)}
        for v, u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1
        
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        ans = []
        cnt = 0
        while q:
            u = q.pop()
            ans.append(u)
            cnt += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        if cnt != numCourses:
            return []
        return ans

        