class Solution:
    
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)
        ans = []
        def dfs(idx, total, curr):
            if total == target:
                ans.append(curr.copy())
                return
            if (total > target) or (idx == n):
                return

            # search from curr i    
            curr.append(candidates[idx])
            dfs(idx + 1, total + candidates[idx], curr)
            curr.pop()

            # remove duplicate i
            while (idx + 1  < n) and (candidates[idx] == candidates[idx+1]):
                idx += 1    
            dfs(idx + 1, total, curr)

        dfs(0, 0, [])
        return ans

        