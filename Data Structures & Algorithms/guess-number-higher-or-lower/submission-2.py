# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l = 1
        r = n
        my_guess = l + (r - l)//2
        while l <= r:
            my_guess = l + (r - l)//2
            pick = guess(my_guess)
            if pick == 0:
                return my_guess
            elif pick == -1:
                r = my_guess - 1
            else:
                l = my_guess + 1
        return my_guess
        