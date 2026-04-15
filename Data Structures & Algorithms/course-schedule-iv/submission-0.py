class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = [[] for _ in range(n)]
        pre = [[-1]*n for _ in range(n)]

        for prereq, crs in prerequisites:
            graph[crs].append(prereq)
            pre[crs][prereq] = 1
        
        def dfs(crs, prereq):
            if pre[crs][prereq] != -1:
                return pre[crs][prereq] == 1
            for v in graph[crs]:
                if v == prereq or dfs(v, prereq):
                    pre[crs][prereq] = 1
                    return True
            pre[crs][prereq] = 0
            return False
        
        res = []
        for u, v in queries:
            res.append(dfs(v, u))

        return res
        