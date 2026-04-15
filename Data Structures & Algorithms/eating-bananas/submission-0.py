class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check_min_hrs(eating_rate):
            total_hrs = 0
            for pile in piles:
                total_hrs += (math.ceil(pile/eating_rate))
                if total_hrs > h:
                    return False
            return True
        ## find optimal eating_rate:
        ## search space: min, max possible eating rate
        ## sorted search space    
        i, j = 1, 1000000001
        optimal_rate = j
        while i <= j:
            mid = i + (j - i)//2
            if check_min_hrs(mid):
                optimal_rate = mid
                j = mid - 1
            else:
                i = mid + 1
        return optimal_rate 
