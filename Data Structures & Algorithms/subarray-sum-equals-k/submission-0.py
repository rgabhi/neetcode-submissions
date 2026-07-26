class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)        
        hm = {}
        hm[0] = 1
        pre = 0
        ans = 0
        for num in nums:
            pre += num
            diff = pre - k
            if diff in hm:
                ans += hm[diff]
            hm[pre] = hm.get(pre, 0)
            hm[pre] += 1
        return ans
                