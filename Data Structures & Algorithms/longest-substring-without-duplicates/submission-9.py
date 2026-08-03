class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        maxl = 0 
        hm = {}
        l = 0
        start_idx = 0
        for i in range(n):
            if s[i] not in hm:
                hm[s[i]] = i
                l += 1
            else:
                if hm[s[i]] < start_idx:
                    hm[s[i]] = i
                    l += 1
                else:
                    maxl = max(maxl, l)
                    l = i - hm[s[i]]
                    start_idx = hm[s[i]] + 1
                    hm[s[i]] = i
        maxl = max(maxl, l)
        return maxl