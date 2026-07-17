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
        #print(dfs(p))
        return dfs(p)==dfs(q)  
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.res = False
        def dfs(curr,sub):
            if not curr:
                if sub:
                    self.res = (self.res) or False
                    return
            else:
                if curr.val == sub.val:
                    print(curr.val)
                    print('resultat_avant:',self.res)
                    #print('le issame:',self.isSameTree(curr,sub))
                    self.res = (self.res) or (self.isSameTree(curr,sub))
                dfs(curr.left,sub)
                dfs(curr.right,sub)
        dfs(root,subRoot)
        return self.res
                