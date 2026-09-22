# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def get_ht(node):
            if not node:
                return 0
            lh = get_ht(node.left)
            rh =  get_ht(node.right)
            if lh == -1 or rh == -1:
                return -1
            if abs(lh - rh) > 1:
                return -1
            return 1 + max(lh, rh)

        return get_ht(root) != -1
            
            

        

        