class Solution:
    def get_subset(self, nums, i, curr_set, all_sets):
        if i == len(nums):
            all_sets.append(curr_set[:])
            return
        curr_set.append(nums[i])
        self.get_subset(nums, i + 1, curr_set, all_sets)
        curr_set.pop()
        self.get_subset(nums, i + 1, curr_set, all_sets)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_sets = []
        self.get_subset(nums, 0, [], all_sets)
        return all_sets
        