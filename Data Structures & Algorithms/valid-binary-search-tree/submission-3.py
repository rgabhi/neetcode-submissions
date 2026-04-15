# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def valid(node, leftLim, rightLim):
            if not node:
                return True
            if not(leftLim < node.val < rightLim):
                return False
            return (
                valid(node.left, leftLim, node.val) and
                valid(node.right, node.val, rightLim)
            )
        return valid(root, -1001, 1001)

        