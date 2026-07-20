# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = [root]
        self.test = [root.val]
        l = [p.val,q.val]
        def dfs(curr,p,q):
            if not curr:
                return
            if (curr.val >= p.val) and (curr.val <= q.val):
                self.res.append(curr)
                self.test.append(curr.val)
                print('p<val<q:',self.test)
                return
            elif (curr.val > p.val) and (curr.val > q.val):
                self.res.append(curr.left)
                self.test.append(curr.left.val)
                print('val>p,q:',self.test)
                dfs(curr.left,p,q)
            elif (curr.val < p.val) and (curr.val < q.val):
                self.res.append(curr.right)
                self.test.append(curr.right.val)
                print('val<p,q:',self.test)
                dfs(curr.right,p,q)
        dfs(root,p,q)
        return self.res[-1]

            
            