class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        import math
        stoneSum = sum(stones)
        n = len(stones)
        target = math.ceil(stoneSum/2)
        dp = {}
        # apprach: get as close as possible to sum//2... 
        def min_sum_path(i, total):
            if total >= target:
                return (total - (stoneSum - total))
            if i == n:
                return abs(total - (stoneSum - total))

            if (i, total) not in dp:
                dp[(i, total)] = min(min_sum_path(i + 1, total), min_sum_path(i + 1, total + stones[i]))    
            return dp[(i, total)]
        
        return min_sum_path(0, 0)

        