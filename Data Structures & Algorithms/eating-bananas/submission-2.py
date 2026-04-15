class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def can_eat(rate):
            curr_time = sum([math.ceil(pile/rate) for pile in piles])
            return curr_time <= h

        l, r = 1, sum(piles)
        ans = r
        while l <= r:
            m = l + (r - l)//2
            if not can_eat(m):
                l = m + 1
            else:
                ans = m
                r = m - 1
        return ans
