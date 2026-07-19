class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return 0
        st = set()
        for num in nums:
            st.add(num)
        maxl = 1
        currl = 1
        currmax = None
        curr = None
        for num in st:
            curr = num
            prev = num - 1
            currl =  1
            while prev in st:
                if prev == currmax:
                    currl = currl + maxl
                    break
                else:
                    currl += 1
                prev -= 1
            if currl > maxl:
                maxl = currl
                currmax = num
        return maxl
            