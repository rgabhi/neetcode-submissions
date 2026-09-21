class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        min_prod = 1
        max_prod = 1
        ans = -float('inf')
        for i in range(n):
            tmp_max = max_prod
            tmp_min = min_prod
            max_prod = max(tmp_max*nums[i], tmp_min*nums[i], nums[i])
            min_prod = min(tmp_max*nums[i], tmp_min*nums[i], nums[i])
            ans = max(ans, max_prod, min_prod)
        return ans

            