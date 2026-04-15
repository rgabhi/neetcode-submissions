class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans = []
        for k in range(n):
            if k > 0 and nums[k] == nums[k-1]:
                continue
            i = k + 1
            j = n - 1
            while i < j:
                if (nums[i] + nums[j]) == -nums[k]:
                    ans.append([nums[i], nums[j], nums[k]])
                    i+= 1
                    j -= 1
                    while (i < j) and nums[i] == nums[i - 1]:
                        i += 1
                    while (i < j) and nums[j] == nums[j + 1]:
                        j -= 1
                elif (nums[i] + nums[j]) > -nums[k]:
                    j -= 1
                else:
                    i += 1
        return ans