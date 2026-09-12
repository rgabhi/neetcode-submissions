class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = {i : [] for i in range(numCourses)}
        pre = [[-1 for _ in range(numCourses)] for _ in range(numCourses)]
        for v, u in prerequisites:
            graph[u].append(v)
            pre[u][v] = 1
        
        # vis = set()
        def dfs(course, prereq):
            # vis.add(u)
            if pre[course][prereq] != -1:
                return pre[course][prereq] == 1

            for v in graph[course]:
                if v == prereq or dfs(v, prereq):
                    pre[course][prereq] = 1
                    return 1
            pre[course][prereq] = 0
            return 0
        ans = []
        for u, v in queries:
            ans.append(dfs(v, u) == 1)
        return ans




        