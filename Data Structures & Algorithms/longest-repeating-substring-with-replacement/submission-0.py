class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        l = 0
        freq = {}
        ans = 0
        for r in range(n):
            freq[s[r]] = 1 + freq.get(s[r], 0)
            max_count = max(freq.values())
            while ((r - l + 1) - max_count) > k:
                freq[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
        return ans
            

        