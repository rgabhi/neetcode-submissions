class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        lmax = [0]*n   
        rmax = [0]*n
        lmax[0] = height[0]
        rmax[n - 1] = height[n - 1]
        for i in range(1, n):
            lmax[i] = max(height[i], lmax[i - 1])
            rmax[n - 1 - i] = max(height[n - 1 - i], rmax[n - i])
        water = 0
        for i in range(1, n - 1):
            curr_water = min(lmax[i - 1], rmax[i + 1]) - height[i]
            if curr_water > 0:
                water += curr_water
        return water
