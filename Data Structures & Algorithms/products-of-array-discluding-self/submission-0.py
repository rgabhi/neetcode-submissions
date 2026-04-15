class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        rsp = [1]*n
        rsp[n - 1] = nums[n - 1]
        for i in range(n - 2, 0, -1):
            rsp[i] = rsp[i + 1]*nums[i]
        rsp[0] = rsp[1]
        lsp = nums[0]
        for i in range(1, n - 1):
            rsp[i] = lsp*rsp[i + 1]
            lsp *= nums[i]
        rsp[n - 1] = lsp
        return rsp

            