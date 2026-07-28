# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        self.root = TreeNode(val = -1)
        def remplir(pre,ino):
            if (not pre) or (not ino):
                return None
            left_ino,right_ino = [],[]
            curr = pre[0]
            dec = True
            for elt in ino:
                if elt == curr:
                    dec = False
                    continue
                if dec:
                    left_ino.append(elt)
                else:
                    right_ino.append(elt)
            #print(left_ino,right_ino)
            node = TreeNode(val = curr)
            #print(self.root.val)
            #root.left = TreeNode(val=-1)
            #root.right = TreeNode(val = -1)
            n = len(left_ino)
            left_pre = pre[1:n+1]
            right_pre = pre[n+1:]
            node.left = remplir(left_pre,left_ino)
            node.right = remplir(right_pre,right_ino)
            return node
        #self.root = TreeNode(val=preorder[0])
        self.root = remplir(preorder,inorder)
        return (self.root)

             
