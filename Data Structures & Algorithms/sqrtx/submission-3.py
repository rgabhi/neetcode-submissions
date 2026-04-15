class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        l, r = 1, x//2
        sqrt = r
        while l <= r:
            m = l + (r - l)//2
            if (x // m) == m:
                return m
            elif (x//m)  > m:
                sqrt = m
                l = m + 1
            else:
                r = m - 1
        return sqrt
        