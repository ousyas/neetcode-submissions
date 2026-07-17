# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth( root: Optional[TreeNode]) -> int:
        if root == None:
            return 0
        else:
            return 1+max(maxDepth(root.right),maxDepth(root.left))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        else:
            if abs(maxDepth(root.right)-maxDepth(root.left)) > 1:
                return False
            else:
                return (self.isBalanced(root.right)) and (self.isBalanced(root.left))