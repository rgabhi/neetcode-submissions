class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n1 = len(text1)
        n2 = len(text2)
        dp = {}


        def longest(i, j):
            if i == n1 or j == n2:
                return 0
            if (i, j) in dp:
                return dp[(i, j)]
            dp[(i, j)] = 0
            if text1[i] == text2[j]:
                dp[(i, j)] = 1 + longest(i + 1, j + 1)
            else:
                dp[(i, j)] = max(longest(i, j + 1), longest(i + 1, j))
            
            return dp[(i, j)]
        
        longest(0, 0)
        return dp[(0, 0)] 

                
                

            
            
        