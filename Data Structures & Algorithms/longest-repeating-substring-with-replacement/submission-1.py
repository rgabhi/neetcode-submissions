class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hm = [0]*26
        n = len(s)
        l = 0
        r = 0
        ans = 0

        while r < n:
            idx =  ord(s[r]) - ord('A')
            hm[idx] += 1
        
            replace = (r - l + 1) - max(hm)
            while (r - l + 1) - max(hm) > k:
                jdx = ord(s[l]) - ord('A')
                hm[jdx] -= 1
                l += 1
            ans = max(ans, r -l + 1)
            r += 1
        return ans
                
