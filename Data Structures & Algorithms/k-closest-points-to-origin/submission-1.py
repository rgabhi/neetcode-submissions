class Solution:
    class point:
        def __init__(self, x, y):
            self.x = x
            self.y = y
            self.dist = x**2 + y**2
        def __lt__(self, other):
            return self.dist < other.dist

        
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        hp = [self.point(x, y) for x, y in points]
        ans = []
        heapq.heapify(hp)
        for i in range(k):
            p = heapq.heappop(hp)
            ans.append([p.x, p.y])
        return ans