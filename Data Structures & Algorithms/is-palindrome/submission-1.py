class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for c in s:
            if c.isalnum():
                arr.append(c.lower())
        n = len(arr)
        i =0
        j = n-1
        while i < j:
            if arr[i] != arr[j]:
                return False
            i += 1
            j -= 1
        return True 
        