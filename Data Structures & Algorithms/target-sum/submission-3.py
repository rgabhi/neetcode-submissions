class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {} # key: (i, total), val = no. of ways till i, for total

        def dfs(i, total):
            if i == n:
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
   
            dp[(i, total)] =(
                dfs(i + 1, total + nums[i]) + 
                dfs(i + 1, total - nums[i])
            )
            return dp[(i, total)]
        
        return dfs(0, 0)


        