class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = {}
        for num in nums:
            cnt[num] = cnt.get(num, 0) + 1
        a = [(k, v) for k, v in cnt.items()]
        a.sort(key=lambda x : x[1])
        a.reverse()
        ans = [x[0] for x in a[:k]]
        return ans
        