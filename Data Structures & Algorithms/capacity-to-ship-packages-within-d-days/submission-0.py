class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def can_ship(curr_cap):
            curr_days = 0
            i = 0
            tmp = 0
            while i < len(weights):
                if tmp + weights[i] <= curr_cap:
                    tmp += weights[i]
                    i += 1
                else:
                    curr_days += 1
                    tmp = 0
            if tmp:
                curr_days += 1
            return curr_days <= days
        
        l = max(weights)
        r = sum(weights)
        ans = r
        while l <= r:
            cap = l + (r - l)//2

            if can_ship(cap):
                ans = cap
                r = cap - 1
            else:
                l = cap + 1
        return ans

