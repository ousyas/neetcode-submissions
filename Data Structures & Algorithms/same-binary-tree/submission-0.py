# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.res = True
        def dfs(curr):
            if not curr:
                return [None]
            else:                
                left = dfs(curr.left)
                right = dfs(curr.right)
                return [curr.val]+left+right
        return dfs(p)==dfs(q)
            