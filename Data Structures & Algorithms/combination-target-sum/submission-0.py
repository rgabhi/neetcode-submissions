class Solution:
    def get_combination(self, nums, i, curr_set, curr_sum, target, all_sets):
        if curr_sum > target:
            return
        if i < len(nums) and curr_sum == target:
            all_sets.add(tuple(curr_set[:]))
        
        if i >= len(nums) and curr_sum != target:
            return

        if i >= len(nums) and curr_sum == target:
                all_sets.add(tuple(curr_set[:]))
                return
        
        curr_set.append(nums[i])
        curr_sum += nums[i]
        self.get_combination(nums, i, curr_set, curr_sum, target, all_sets)
        self.get_combination(nums, i + 1, curr_set, curr_sum, target, all_sets)
        curr_set.pop()
        curr_sum -= nums[i]
        self.get_combination(nums, i + 1, curr_set, curr_sum, target, all_sets)
            

    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        all_sets = set()
        self.get_combination(nums, 0, [], 0, target, all_sets)
        all_sets = [list(x) for x in all_sets]
        return all_sets
        