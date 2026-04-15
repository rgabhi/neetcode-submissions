class Solution:
    def tribonacci(self, n: int) -> int:
        dp = {}
        def fun(num):
            if num <= 0:
                return 0
            if num == 1 or num == 2:
                return 1
            if num in dp:
                return dp[num]
            dp[num] = fun(num - 1) + fun(num - 2) + fun(num - 3)
            return dp[num]
            
        return fun(n)