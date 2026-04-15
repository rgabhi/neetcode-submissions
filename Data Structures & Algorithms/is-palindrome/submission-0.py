class Solution:
    def isPalindrome(self, s: str) -> bool:
        chars = []
        for c in s:
            od = ord(c.lower())
            if ord('0') <= od <= ord('9'):
                chars.append(c)
            elif ord('a') <= od <= ord('z'):
                chars.append(c.lower())
        i, j = 0, len(chars) - 1
        print(chars)
        while i < j:
            if chars[i] != chars[j]:
                return False
            i += 1
            j -= 1
        return True