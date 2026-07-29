class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = []
        k = n-1
        while k >= 0:
            i = 0
            j = k - 1
            while i < j:
                curr = nums[i] + nums[j]
                if curr == -nums[k]:
                    ans.append([nums[i], nums[j], nums[k]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i-1] and i < k:
                        i += 1
                    while nums[j] == nums[j+1] and j >= 0:
                        j -= 1
                        
                elif curr < -nums[k]:
                    i += 1
                else:
                    j -= 1
            k -= 1
            while nums[k] == nums[k + 1] and k >= 0:
                k -= 1
        return ans
            


        