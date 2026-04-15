class Solution:
    def getSubXor(self, nums, i, currXor):
        if i == len(nums):
            return 0
        currAns = 0
        currXor ^= nums[i]
        currAns += currXor
        currAns += self.getSubXor(nums, i + 1, currXor)
        currXor ^= nums[i]
        currAns += self.getSubXor(nums, i + 1, currXor)
        return currAns
    def subsetXORSum(self, nums: List[int]) -> int:
        return self.getSubXor(nums, 0, 0)
        