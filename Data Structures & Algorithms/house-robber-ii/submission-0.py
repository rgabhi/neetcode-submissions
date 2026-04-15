class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))
    
    def helper(self, nums):
        max_rob_till_prev1 = 0
        max_rob_till_prev2 = 0
        for money in nums:
            new_rob = max(max_rob_till_prev2 + money, max_rob_till_prev1)
            max_rob_till_prev2 = max_rob_till_prev1
            max_rob_till_prev1 = new_rob
        return max(max_rob_till_prev1, max_rob_till_prev2)