class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 1 or x == 0:
            return x
        l = 1
        r = x
        m = l + (r - l)//2
        ans = -1
        while l <= r:
            m = l + (r - l)//2
            # print(l, r)
            if (m) == (x//m):
                # print(m)
                return m
            elif m > x//m:
                r = m - 1
            else:
                ans = m
                l = m + 1
        
        return ans
        