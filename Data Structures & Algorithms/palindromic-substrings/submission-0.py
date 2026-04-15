class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        cnt = 0
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n):
            dp[i][i] = True
            cnt+=1
            if i < n - 1 and s[i] == s[i + 1]:
                dp[i][i + 1] = True
                cnt += 1
        # single centre
        for i in range(n):
            l = i - 1 
            r = i + 1 
            while  l >= 0 and r < n:
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    cnt += 1
                else:
                    break
                l -= 1
                r += 1

        # double centre
        for i in range(n - 1):
            if dp[i][i + 1] == False:
                continue
            l = i - 1 
            r = i + 2 
            while l >= 0 and r < n:
                if s[l] == s[r] and dp[l + 1][r - 1]:
                    dp[l][r] = True
                    cnt += 1
                else:
                    break
                l -= 1
                r += 1
        return cnt
        
        

        