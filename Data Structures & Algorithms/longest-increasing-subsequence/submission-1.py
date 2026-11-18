class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp[i] => lis len ending at idx i
        n = len(nums)
        dp = [0 for _ in range(n)]
        for i in range(n):
            dp[i] = 1
        ans = 1
        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(1 + dp[j], dp[i])
            ans = max(ans,dp[i])
        return ans

        
        