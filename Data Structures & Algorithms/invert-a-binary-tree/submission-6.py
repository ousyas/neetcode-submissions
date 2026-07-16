# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        elif (root.left == None) and (root.right == None):
            return root
        #elif (root.right.right == None) or (root.right.left == None) or (root.left.right == None) or (root.left.right == None):
            #root.right,root.left = root.left,root.right
            #return root
        else:
            root.right,root.left = self.invertTree(root.left),self.invertTree(root.right)
            return root

