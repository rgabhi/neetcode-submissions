class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.hp = sorted(nums)
        self.k = k
        if len(self.hp) > self.k:
            self.hp = self.hp[-self.k:]
        
    def add(self, val: int) -> int:
        heapq.heappush(self.hp, val)
        if len(self.hp) > self.k:
            heapq.heappop(self.hp)
        return self.hp[0]
    
        
        
