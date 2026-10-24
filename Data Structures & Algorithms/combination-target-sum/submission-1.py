class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        ans = []
        def choose(i, curr, tmp):
            if i == n or curr > target:
                return
            if curr == target:
                ans.append(list(tmp))
                return
            
            #consider i
            tmp.append(nums[i])
            choose(i, curr + nums[i], tmp)
            tmp.pop()
            choose(i + 1, curr, tmp)
        choose(0, 0, [])
        return ans

            
            

        