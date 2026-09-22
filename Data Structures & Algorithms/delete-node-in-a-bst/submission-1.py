# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        if key == root.val:
            l = root.left
            r = root.right
            if l: 
                root = l
                tmp = root.right
                if not tmp:
                    root.right = r
                else:
                    while tmp.right:
                        tmp = tmp.right
                    tmp.right = r
            else:
                return r

        return root

        