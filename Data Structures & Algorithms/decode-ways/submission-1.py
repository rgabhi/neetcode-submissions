class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import lru_cache
        n = len(s)
        @lru_cache(maxsize=None)
        def ways(idx):
            if idx == n:
                return 1
            if s[idx] == '0':
                return 0
            
            if idx == n - 1:
                return 1

            ans = ways(idx + 1)

            if (int(s[idx: idx + 2]) <= 26):
                ans += ways(idx + 2)
            return ans 
        
        return ways(0)