class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1]*n

        def max_rob(idx):
            if idx >= n:
                return 0
            if dp[idx] != -1:
                return dp[idx]
            rob_1 = nums[idx] + max_rob(idx + 2)
            rob_2 = max_rob(idx + 1)
            dp[idx] = max(rob_1, rob_2)
            return dp[idx]
        return max_rob(0) 
        