class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        hm = {}
        for i in range(n):
            if nums[i] not in hm:
                hm[nums[i]] = 0
            hm[nums[i]] += 1
        pq = []
        for num in hm:
            heapq.heappush(pq, (hm[num], num))
            if len(pq) > k:
                heapq.heappop(pq)
        return [x[1] for x in pq]
        