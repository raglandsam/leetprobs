# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):

        def dfs(root,l):

            if not root :
                return 
            elif not(root.left) and not(root.right):
                l.append(root.val)
            else:
                dfs(root.left,l)
                dfs(root.right,l)
    
        l1,l2=[],[]
        dfs(root1,l1)
        dfs(root2,l2)
        return l1==l2
        
            

        