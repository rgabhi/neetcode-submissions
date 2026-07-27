class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n):
            if nums[i] < 0:
                nums[i] = 0
        for i in range(n):
            if 1 <= abs(nums[i]) <= n:
                idx = abs(nums[i])- 1
                if nums[idx] != 0:
                    nums[idx] = -abs(nums[idx])
                else:
                    nums[idx] = -(n+1)
        ans = n + 1
        print(nums)
        for i in range(n):
            if nums[i] >= 0:
                ans = i + 1
                return ans
        return ans 