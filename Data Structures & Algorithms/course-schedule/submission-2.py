class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree = [0]*numCourses
        graph = {i : [] for i in range(numCourses)}
        q = deque()
        for c, d in prerequisites:
            graph[d].append(c)
            indegree[c] += 1
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        cnt = 0
        while q:
            u = q.popleft()
            cnt += 1
            for v in graph[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)
        return cnt == numCourses
            

        