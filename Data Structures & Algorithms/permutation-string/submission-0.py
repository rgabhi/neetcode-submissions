class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        og = {}
        for c in s1:
            og[c] = og.get(c, 0) + 1

        if len(s1) > len(s2):
            return False
        hm = {}
        l = 0
        r = 0
        n = len(s2)
        while r < n:
            currl = r - l + 1
            hm[s2[r]] = hm.get(s2[r], 0) + 1
            if currl < len(s1):
                r += 1
            else:
                flag= True
                for c in og:
                    if c not in hm:
                        flag = False
                        break
                    if og[c] != hm[c]:
                        flag = False
                        break
                if flag:
                    # print(l, r)
                    # print(s1)
                    # print(s2[l:r + 1])
                    return True
                else:
                    hm[s2[l]] -= 1
                    l += 1
                    r += 1
        return False



        