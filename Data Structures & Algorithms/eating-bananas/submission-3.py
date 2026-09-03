class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = sum(piles)
        ans = r
        def can_eat(rate):
            time = 0
            for pile in piles:
                time += math.ceil(pile/rate)
            return time <= h


        while l <= r:
            m = l + (r - l)//2
            if can_eat(m):
                ans = m
                r = m - 1
            else:
                l = m + 1
        return ans
        
        