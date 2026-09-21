class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = {}
        def check_in_dict(i):
            if i > n:
                return False
            if i == n:
                return True
            
            if i not in dp:
                dp[i] = False
                for word in wordDict:
                    m = len(word)
                    if i + m > n:
                        continue
                    flag = True
                    for k in range(m):
                        if word[k] != s[i + k]:
                            flag = False
                            break
                    if flag:
                        dp[i] = dp[i] or check_in_dict(i + m)
            return dp[i]
        return check_in_dict(0)
                    
                

        