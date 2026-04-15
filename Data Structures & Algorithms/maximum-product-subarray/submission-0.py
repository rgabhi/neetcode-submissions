class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        res = max(nums)
        currMax, currMin = 1, 1
        for num in nums:
            tmpMax = currMax*num
            currMax = max(currMax*num, currMin*num, num)
            currMin = min(tmpMax, currMin*num, num)
            res = max(res, currMax)
        return res

