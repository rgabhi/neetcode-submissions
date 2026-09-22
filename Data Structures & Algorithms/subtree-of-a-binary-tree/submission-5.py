# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        
        if self.is_same(root, subRoot):
            return True
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))
    
    def is_same(self, root, sub):
        if not root and not sub:
            return True
        if not root or not sub:
            return False
        l = self.is_same(root.left, sub.left)
        r = self.is_same(root.right, sub.right)
        return root.val == sub.val and l and r
