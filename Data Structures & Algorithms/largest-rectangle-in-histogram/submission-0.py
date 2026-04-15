class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        n = len(heights)
        maxArea = 0
        for i in range(n):           
            start = i
            while stack and heights[i] < stack[-1][1]:
                idx, h = stack.pop()
                start = idx
                maxArea = max(maxArea, h*(i - start))
            stack.append((start, heights[i]))
        
        while stack:
            i, h = stack.pop()
            maxArea = max(maxArea, h*(n - i))
        return maxArea
        

                    
                