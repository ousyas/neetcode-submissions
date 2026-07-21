# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 1   
        def bfs(root):
            if not root:
                return
            q = deque([root])
            c = deque([root])
            while q:
                node = q.popleft()
                comp = c.popleft()
                if node.left:
                    if comp.val > node.left.val:
                        c.append(comp)
                    else:
                        self.res+=1
                        c.append(node.left)
                    q.append(node.left)    
                if node.right:
                    if comp.val > node.right.val:
                        c.append(comp)
                    else:
                        self.res+=1
                        c.append(node.right)
                    q.append(node.right)
        bfs(root)
        return self.res

            