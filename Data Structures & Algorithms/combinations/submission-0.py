class Solution:
    def get_combination(self, n, k, i, curr_set, all_sets):
        if len(curr_set) == k:
            all_sets.append(curr_set[:])
            return
        if i > n or len(curr_set) > k:
            return
        curr_set.append(i)
        self.get_combination(n, k, i + 1, curr_set, all_sets)
        curr_set.pop()
        self.get_combination(n, k, i + 1, curr_set, all_sets)

    def combine(self, n: int, k: int) -> List[List[int]]:
        all_sets = []
        self.get_combination(n, k, 1, [], all_sets)
        return all_sets
        

        