class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        st = []
        ans= 0
        
        for i in range(n+1):
            while st and (i == n or heights[st[-1]] >= heights[i]):
                ht = heights[st.pop()]
                wid = i if not st else i - st[-1] - 1
                ans = max(ans, ht*wid)
            st.append(i)
        return ans
           
        
    

        