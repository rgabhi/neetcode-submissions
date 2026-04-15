class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp = [-num for num in nums]
        heapq.heapify(hp)
        ans = -1
        for i in range(k):
            ans = -heapq.heappop(hp)
        return ans

        