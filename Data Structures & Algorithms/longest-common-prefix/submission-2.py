class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = strs[0]
        n = len(strs)

        for i in range(1, n):
            min_len = min(len(longest_prefix), len(strs[i]))
            if min_len == 0:
                return ""
            longest_prefix = longest_prefix[:min_len]
            for k in range(min_len):
                if longest_prefix[k] != strs[i][k]:
                    longest_prefix = longest_prefix[:k]
                    break
        return longest_prefix    


        