class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rprod = [1]*(n + 1)
        for i in range(n - 1, -1, -1):
            rprod[i] = rprod[i+1]*nums[i]
        
        lprod = 1
        ans = [1]*n
        for i in range(n):
            ans[i] = lprod*rprod[i+1]
            lprod *= nums[i]
        return ans

        