# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        k = 0
        dic1 = {}
        dic2 = {}
        def parc(curr,k):
            if not curr:
                #if k not in dic1.keys():
                    #dic1[k] = [None]
                #else:
                    #dic1[k].append(None)
                return   
            if k not in dic1.keys():
                dic1[k] = [curr.val]
            else:
                dic1[k].append(curr.val)
            k+=1
            parc(curr.left,k)
            parc(curr.right,k)
        parc(root,k)
        return list(dic1.values())
