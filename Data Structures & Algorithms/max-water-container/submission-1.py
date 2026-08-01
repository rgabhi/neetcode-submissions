class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        curr = 0
        ans = 0
        while i < j:
            curr = min(heights[i], heights[j])*(j - i)
            ans = max(ans, curr)
            if heights[i] >=  heights[j]:
                j -= 1
            else:
                i += 1
        return ans    
                
        