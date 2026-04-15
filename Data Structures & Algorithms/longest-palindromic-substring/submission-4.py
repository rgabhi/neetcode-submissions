class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        f, e = 0, 0
        maxL = 1
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            if i < n-1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                maxL = 2
                f, e = i, i + 1

        for i in range(n):
            l = i - 1
            r = i + 1
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]
                    if dp[l][r] and maxL < (r - l + 1):
                        maxL = r - l + 1
                        f, e = l, r
                else:
                    break
                l -= 1
                r += 1
                            
        for i in range(n-1):
            if dp[i][i + 1] == False:
                continue
            l = i - 1
            r = i + 2
            while l >= 0 and r < n:
                if s[l] == s[r]:
                    dp[l][r] = dp[l + 1][r - 1]
                    if dp[l][r] and maxL < (r -l + 1):
                        maxL = r - l + 1
                        f, e = l, r
                else:
                    break
                l -= 1
                r += 1
        return s[f:e + 1]

            
