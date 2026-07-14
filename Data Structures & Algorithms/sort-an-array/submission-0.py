class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge_sort(l , r):
            if l >= r:
                return
            m = (l + r)//2
            merge_sort(l, m)
            merge_sort(m + 1, r)
            merge(l, m, r)

        def merge(l, m, r):
            i, j, k = l, m + 1, 0
            tmp = [0]*(r - l + 1)
            while i <= m and j <= r:
                if nums[i] <= nums[j]:
                    tmp[k] = nums[i]
                    k += 1
                    i += 1
                else:
                    tmp[k] = nums[j]
                    k += 1
                    j += 1
            while i <= m:
                tmp[k] = nums[i]
                k += 1
                i += 1
            while j <= r:
                tmp[k] = nums[j]
                k += 1
                j += 1
            for i in range(l, r + 1):
                nums[i] = tmp[i - l]
        
        merge_sort(0, len(nums)-1)
        return nums
        
        