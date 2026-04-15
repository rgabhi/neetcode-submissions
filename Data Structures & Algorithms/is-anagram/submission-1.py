class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_arr = [0]*26
        t_arr = [0]*26
        for i in range(len(s)):
            idx = ord(s[i]) - ord('a')
            s_arr[idx] += 1
        for i in range(len(t)):
            idx = ord(t[i]) - ord('a')
            t_arr[idx] += 1
        for i in range(26):
            if s_arr[i] != t_arr[i]:
                return False
        return True
