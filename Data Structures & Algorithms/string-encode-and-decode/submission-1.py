class Solution:

    def encode(self, strs: List[str]) -> str:
        ans = ""
        for s in strs:
            ans = ans + str(len(s)) + "#" + s
        return ans

    def decode(self, s: str) -> List[str]:
        ans = []
        n = len(s)
        i = 0
        j = 0
        while i < n:
            while s[j] != '#':
                j +=1
            l = int(s[i:j])
            ans.append(s[j + 1: j + 1 + l])
            i = j + l + 1
            j = i
        return ans
            

