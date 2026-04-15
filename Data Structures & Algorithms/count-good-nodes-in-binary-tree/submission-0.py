# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def cnt_good(self, root, curr_max):
        if not root:
            return 0
        if root.val >= curr_max:
            curr_max = max(root.val, curr_max)
            return 1 + self.cnt_good(root.left, curr_max) + self.cnt_good(root.right, curr_max)
        return self.cnt_good(root.left, curr_max) + self.cnt_good(root.right, curr_max)
        
    def goodNodes(self, root: TreeNode) -> int:
        return self.cnt_good(root, -101)
        
        