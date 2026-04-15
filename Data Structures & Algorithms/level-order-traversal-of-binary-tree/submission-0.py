# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append(root)
        ans = []
        level_ans = []
        level = 0
        while q:
            sz = len(q)
            level_ans = []
            while sz > 0:
                node = q.popleft()
                level_ans.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                sz -= 1
            ans.append(level_ans)
            level += 1
        return ans
        
            

        
        