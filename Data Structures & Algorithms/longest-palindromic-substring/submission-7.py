class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        res = 0
        resl = 1
        #odd
        for i in range(n):
            f = i+1
            b = i - 1
            currl = 1
            while (b >= 0) and (f < n):
                if s[f] == s[b]:
                    f += 1
                    b -= 1
                    currl += 2
                else:
                    break
            if currl > resl:
                res = b + 1
                resl = currl
            # print("odd", i, res, resl)
        
        #even
        for i in range(n-1):
            if s[i] == s[i+1]:
                currl = 2
                b = i - 1
                f = i + 2
                while (b >= 0 ) and (f < n):
                    if s[f] == s[b]:
                        f += 1
                        b -= 1
                        currl += 2
                    else:
                        break
                if currl > resl:
                    res = b + 1
                    resl = currl
            # print("even", i, res, resl)
        return s[res:res + resl]