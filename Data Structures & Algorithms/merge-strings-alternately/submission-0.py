class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        m = len(word1)
        n = len(word2)
        i =0
        j =0
        ans = []
        while i < m and j < n:
            ans.append(word1[i])
            ans.append(word2[j])
            i += 1
            j += 1
        ans = "".join(ans)
        if i < m:
            ans = ans + word1[i:]
        if j < n:
            ans = ans + word2[j:]
        return ans
            
