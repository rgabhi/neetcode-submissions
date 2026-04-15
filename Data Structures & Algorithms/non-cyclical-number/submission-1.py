class Solution:
    def _sum_squares(self, n):
        square_sum = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            digit_square = (digit*digit)
            square_sum +=  digit_square
        return square_sum
            
    def isHappy(self, n: int) -> bool:
        seen_nums = set()
        while n not in seen_nums:
            seen_nums.add(n)
            n = self._sum_squares(n)
            if n == 1:
                return True
        print(seen_nums)
        return False
        
        