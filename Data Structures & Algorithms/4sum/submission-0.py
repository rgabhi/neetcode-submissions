class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        l = n - 1
        ans = []
        while l >= 0:
            k = l - 1
            while k >= 0:
                i = 0
                j = k - 1
                while i < j:
                    curr = nums[i] + nums[j] + nums[k] + nums[l]
                    if curr == target:
                        ans.append([nums[i], nums[j], nums[k], nums[l]])
                        i += 1
                        j -= 1
                        while nums[i] == nums[i-1] and i < j:
                            i += 1
                        while nums[j] == nums[j + 1] and j > i:
                            j -= 1
                    elif curr < target:
                        i += 1
                    else:
                        j -= 1
                k -= 1
                while k >= 0 and nums[k] ==  nums[k + 1]:
                    k -=1 
            l -= 1
            while l >= 0 and nums[l] == nums[l + 1]:
                l -= 1
        return ans       
