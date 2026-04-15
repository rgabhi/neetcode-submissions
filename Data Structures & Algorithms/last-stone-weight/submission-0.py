class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        pq = [-stone for stone in stones]
        heapq.heapify(pq)
        while pq:
            if len(pq) == 1:
                return -pq[0]
            stone1 = -heapq.heappop(pq)
            stone2 = -heapq.heappop(pq)
            if stone1 != stone2:
                heapq.heappush(pq, -(stone1 - stone2))
        return 0


        