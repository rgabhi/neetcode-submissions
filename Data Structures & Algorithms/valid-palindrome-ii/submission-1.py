class Solution:
    def _isPalindrome(self, s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def validPalindrome(self, s: str) -> bool:
        l , r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                return (
                    self._isPalindrome(s, l + 1, r) or
                    self._isPalindrome(s, l, r - 1)
                )
            l += 1
            r -= 1
        return True


    
        