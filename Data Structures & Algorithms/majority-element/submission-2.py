class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        bits = [0]*32
        for num in nums:
            for i in range(32):
                bits[i] += ((num >> i) & 1)
        ans = 0
        for i in range(32):
            if bits[i] > (n//2):
                if i != 31:
                    ans |= (1<<i)
                else:
                    ans -= (1<<i)
        return ans
