class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = digits[::-1]
        n = len(digits)
        curr = 0
        carry = 1
        for i in range(n):
            curr = digits[i] + carry
            carry = curr // 10
            curr = curr % 10
            digits[i] = curr
        if carry != 0:
            digits.append(carry)
        digits = digits[::-1]
        return digits