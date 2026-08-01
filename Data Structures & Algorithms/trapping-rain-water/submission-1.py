class Solution:
    def trap(self, height: List[int]) -> int:
        water = 0
        n = len(height)
        rmax = [0]*(n)
        for i in range(n-2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i+1])
        lmax = 0
        for i in range(1, n):
            lmax = max(lmax, height[i-1])
            bound = min(lmax, rmax[i])
            if height[i] < bound:
                water += bound - height[i]
        return water