class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        j = 0
        k = 0
        for i in range(n):
            if nums[i] != val:
                nums[j] = nums[i]
                j += 1
                k += 1
        return k
        
        

        