class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        st = set()
        ans = 1
        for num in nums:
            if num > 0:
                ans = max(ans, num + 1)
                st.add(num)
        tmp = ans - 1
        while tmp > 0:
            if tmp in st:
                tmp -= 1
            else:
                ans = tmp
                tmp -=1 
        return ans