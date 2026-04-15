class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n == 0:
            return 0
        longest = ""
        curr = ""
        for i in range(n):
            curr = s[i]
            for j in range(i + 1, n):
                if s[j] not in curr:
                    curr += s[j]
                else:
                    break
            if len(curr) > len(longest):
                longest = curr
        print(longest)
        return len(longest)
        