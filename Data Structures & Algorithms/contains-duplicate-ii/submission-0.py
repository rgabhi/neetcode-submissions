class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        i = 0
        st = set()
        k = min(n, k)
        for i in range(k):
            if nums[i] in st:
                return True
            else:
                st.add(nums[i])
        for i in range(k, n):
            if nums[i] in st:
                return True
            else:
                st.add(nums[i])
            st.remove(nums[i - k])
        return False
            


        