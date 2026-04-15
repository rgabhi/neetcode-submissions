class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = dict()
        for i in range(len(nums)):
            if target - nums[i] in hm:
                if hm[target - nums[i]] != i:
                    return sorted([i, hm[target - nums[i]]])
            else:
                hm[nums[i]] = i
        return []